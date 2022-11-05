from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', views.profile, name='my_profile'),
    path('<str:username>/', views.other_profile, name='other_profile'),
]