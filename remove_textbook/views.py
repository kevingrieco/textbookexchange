from django.shortcuts import render, redirect
from post_textbook.models import Department, Course, Textbook

# Create your views here.

def delete_confirm(request, pk):
    textbook = Textbook.objects.get(pk=pk)
    view = request.POST.get('view')
    if request.user == textbook.user:
        return render(request, 'remove_textbook/delete_confirm.html', {'textbook':textbook, 'view':view})
    else:
        return redirect(view)

def delete_textbook(request, pk):
    textbook = Textbook.objects.get(pk=pk)
    course = textbook.course
    department = textbook.department
    view = request.POST.get('view')
    if textbook.user == request.user:
        textbook.delete()
        if len(course.textbooks.all()) == 0:
            course.delete()
        if len(department.courses.all()) == 0:
            department.delete()
    return redirect(view)
