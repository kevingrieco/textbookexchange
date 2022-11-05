from django.urls import path
from . import views

app_name = 'direct_messages'

urlpatterns = [
    path('', views.message_user, name='message_user'),
]