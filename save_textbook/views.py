from django.shortcuts import render, redirect
from post_textbook.models import Department, Course, Textbook

# Create your views here.

def save_textbook(request, pk):
    textbook = Textbook.objects.get(pk=pk)
    course = textbook.course
    department = textbook.department
    view = request.POST.get('view')
    if textbook.user == request.user:
        textbook.save()
        if len(course.textbooks.all()) == 0:
            course.save()
        if len(department.courses.all()) == 0:
            department.save()
    return redirect(view)
