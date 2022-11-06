from django.urls import path
from . import views

app_name = 'direct_messages'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('message/', views.message_user, name='message_user'),
    path('<int:pk>/', views.view_conversation, name='view_conversation'),
    path('send/', views.send_message, name='send_message'),
]