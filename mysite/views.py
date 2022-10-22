from django.shortcuts import render
from post_textbook.models import Department

def index_view(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
    }
    return render(request, 'index.html', context)