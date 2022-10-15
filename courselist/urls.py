from django.urls import path
from . import views

app_name = 'courselist'

urlpatterns= [
    path('', views.HomePageView.as_view(template_name="courselist/index.html"), name='index'),
]