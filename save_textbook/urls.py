from django.urls import path
from . import views

app_name = 'remove_textbook'

urlpatterns = [
    path('<int:pk>/delete/', views.save_textbook, name='save_textbook'),
    ]