from django.urls import path
from . import views

app_name = 'post_textbook'

urlpatterns = [
    path('', views.choose_department, name='choose_department'),
    path('choose_course/', views.load_courses, name='choose_course'),
    path('choose_course/textbook_details/', views.textbook_info, name='textbook_details')
]