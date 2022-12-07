from django.urls import path
from . import views
from friends.views import view_friend_requests, request_friend, handle_friend_request, remove_friend, view_friends

app_name = 'user_profile'

urlpatterns = [
    path('', views.profile, name='my_profile'),
    path('friend_requests/', view_friend_requests, name='friend_requests'),
    path('friends/', view_friends, name='view_friends'),
    path('user/<str:username>/', views.other_profile, name='other_profile'),
    path('send_request/', request_friend, name='request_friend'),
    path('handle_request/', handle_friend_request, name='handle_friend_request'),
    path('remove_friend/', remove_friend, name='remove_friend'),
]