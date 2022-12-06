from django.urls import path
from . import views

app_name = 'save_textbook'

urlpatterns = [
    path('<int:pk>/save_confirm/', views.save_confirm, name='save_confirm'),
    path('<int:pk>/save/', views.save_textbook, name='save_textbook')
    ]