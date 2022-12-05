from django.urls import path
from . import views

app_name = 'remove_textbook'

urlpatterns = [
    path('<int:pk>/delete_confirm/', views.delete_confirm, name='delete_confirm'),
    path('<int:pk>/delete/', views.delete_textbook, name='delete_textbook'),
    ]