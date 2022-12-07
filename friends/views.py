from django.shortcuts import render, redirect
from .models import Friends, FriendRequests
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()
users = User.objects.all()

def request_friend(request):
    user = User.objects.get(pk=request.POST.get('pk'))
    try:
        friend_requests = FriendRequests.objects.get(user=user)
    except:
        friend_requests = FriendRequests(user=user)
        friend_requests.save()
    is_requested = request.POST.get('is_requested') == 'True'
    if is_requested:
        friend_requests.users.remove(request.user)
    else:
        friend_requests.users.add(request.user)
    return redirect('user_profile:other_profile', user.username)

def view_friend_requests(request):
    try:
        friend_requests = FriendRequests.objects.get(user=request.user)
    except:
        friend_requests = FriendRequests(user=request.user)
        friend_requests.save()
    friend_requests = friend_requests.users.all()
    return render(request, 'user_profile/friend_requests.html', {'friend_requests': friend_requests, 'empty': len(friend_requests)==0, })

def handle_friend_request(request):
    user = User.objects.get(pk=request.POST.get('pk'))
    accept = request.POST.get('accept') == 'True'
    friend_requests = FriendRequests.objects.get(user=request.user)
    friend_requests.users.remove(user)
    if accept:
        user.friends.users.add(request.user)
        request.user.friends.users.add(user)
    return redirect('user_profile:friend_requests')

def remove_friend(request):
    user = User.objects.get(pk=request.POST.get('pk'))
    user.friends.users.remove(request.user)
    request.user.friends.users.remove(user)
    return redirect(request.POST.get('view'))

def view_friends(request):
    try:
        friends = Friends.objects.get(user=request.user)
    except:
        friends = Friends(user=request.user)
        friends.save()
    friends = friends.users.all()
    return render(request, 'user_profile/friends.html', {'friends': friends, 'empty': len(friends)==0})