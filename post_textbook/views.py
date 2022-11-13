
from django.shortcuts import render, redirect
from .models import Department, Course, Textbook
import requests

# Create your views here.

def choose_department(request):
    textbooks = Textbook.objects.all()
    mn_req = requests.get('http://luthers-list.herokuapp.com/api/deptlist?format=json')
    depts = []
    for department in mn_req.json():
        depts.append(department['subject'])
    context = {
        'current_textbooks': textbooks,
        'course_depts': depts,
    }
    return render(request, 'post_textbook/textbook_list.html', context)

def load_courses(request):
    dept = request.POST.get('dept')
    if dept is None:
        return redirect('post_textbook:choose_department')
    courses = []
    courses_raw = requests.get(f"http://luthers-list.herokuapp.com/api/dept/{dept}?format=json")
    courses_dict = courses_raw.json()
    for course in courses_dict:
        to_add = f"{dept} {course['catalog_number']}: {course['description']}"
        if not to_add in courses:
            courses.append(to_add)
    context = {
        'dept': dept,
        'courses': courses,
    }
    return render(request, 'post_textbook/choose_course.html', context)

def textbook_info(request):
    department_name = request.POST.get('department')
    course_name = request.POST.get('course')

    if Department.objects.filter(name=department_name).exists():
        department = Department.objects.get(name=department_name)
    else:
        department = Department(name=department_name)
        department.save()
    if Course.objects.filter(name=course_name).exists():
        course = Course.objects.get(name=course_name)
    else:
        course = Course(name=course_name, department=department)
        course.save()
    
    user = request.user

    title = request.POST.get('title')
    author = request.POST.get('author')
    publisher = request.POST.get('publisher')
    edition = request.POST.get('edition')
    year = request.POST.get('year')
    ISBN = request.POST.get('ISBN')

    cover_image_link = f"https://covers.openlibrary.org/b/isbn/{ISBN}-L.jpg?default=false"
    cover_or_404 = requests.get(cover_image_link)
    if cover_or_404.status_code == 404:
        cover = "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/3166594/book-clipart-md.png"
    else:
        cover = cover_image_link
    

    new_textbook = Textbook(
        department=department, 
        course=course, 
        user=user,
        title=title, 
        author=author, 
        publisher=publisher, 
        edition=edition, 
        year=year,
        ISBN=ISBN,
        cover=cover
        )
    new_textbook.save()
    return redirect('index')
