
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
    

    title = request.POST.get('title')
    author = request.POST.get('author')
    publisher = request.POST.get('publisher')
    edition = request.POST.get('edition')
    year = request.POST.get('year')
    ISBN = request.POST.get('ISBN')
    new_textbook = Textbook(
        department=department, 
        course=course, 
        title=title, 
        author=author, 
        publisher=publisher, 
        edition=edition, 
        year=year,
        ISBN=ISBN)
    new_textbook.save()
    return redirect('index')

# def save_course_info(request):
#     course = request.POST.get('course')
#     new_course = Course()
#     new_course.course_name = course
#     new_course.save()
#     return redirect(upload_textbook)

    
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

# class TextbookListView(ListView):
#     model = TextbookUpload
#     context_object_name = 'textbooks'

# class TextbookCreateView(CreateView):
#     model = TextbookUpload
#     fields = ('department', 'number', 'class_description', 'title', 'author', 'year', 'edition')
#     form_class = TextbookForm
#     success_url = reverse_lazy('textbook_changelist')

# class TextbookUpdateView(UpdateView):
#     model = TextbookUpload
#     fields = ('department', 'number', 'class_description', 'title', 'author', 'year', 'edition')
#     form_class = TextbookForm
#     success_url = reverse_lazy('textbook_changelist')
