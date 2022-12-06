from django.urls import path
from . import views

app_name = 'save_textbook'

urlpatterns = [
    path('', views.favorites, name='favorites'),
    path('<int:pk>/save/', views.save_textbook, name='save_textbook'),
    ]