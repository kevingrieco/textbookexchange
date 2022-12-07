from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('send_request/', views.request_friend, name='request_friend'),
    path('handle_request/', views.handle_friend_request, name='handle_friend_request'),
    path('remove_friend/', views.remove_friend, name='remove_friend'),
]