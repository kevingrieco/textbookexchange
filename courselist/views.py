from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from .models import Course
import requests

# Create your views here.

class HomePageView(TemplateView):

    def get_context_data(self, *args, **kwargs):
        template_name = 'courselist/index.html'
        mn_req = requests.get('http://luthers-list.herokuapp.com/api/deptlist?format=json')
        courses = []
        for course in mn_req.json():
            courses.append(course['subject'])
        full_names = {

        }
        for course in courses:
            full_names[course] = "Full"
        context = {
            'courses_list': courses
        }
        return context