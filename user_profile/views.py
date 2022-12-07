from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from friends.models import Friends, FriendRequests
from django.contrib.auth import get_user_model


User = get_user_model()
users = User.objects.all()
# Gets textbook from database

def get_user_textbooks(user):
    textbooks = user.textbooks.all()
    departments = {}
    for textbook in textbooks:
        if not textbook.department in departments:
            departments[textbook.department] = {textbook.course: []}
        departments[textbook.department][textbook.course].append(textbook)
    return departments

#gets your profile information
def profile(request):
    social_account = SocialAccount.objects.filter(user=request.user)
    departments = get_user_textbooks(request.user)

    context = {
        'social_account': social_account,
        'departments': departments,
        'empty': len(departments) == 0,
    }
    return render(request, 'user_profile/profile.html', context)

#gets other profile info
def other_profile(request, username):
    if username == request.user.username:
        return redirect('user_profile:my_profile')
    user_real = users.get(username=username)
    departments = get_user_textbooks(user_real)
    social_account = SocialAccount.objects.filter(user=user_real)
    if social_account:
        name = social_account[0].extra_data['name']
    elif user_real.first_name:
        name = user_real.first_name
        if user_real.last_name:
            name += " " + user_real.last_name
    else:
        name = username

    try:
        friend_requests = FriendRequests.objects.get(user=user_real)
    except:
        friend_requests = FriendRequests(user=user_real)
        friend_requests.save()
    try:
        user_real_friends = Friends.objects.get(user=user_real)
    except:
        user_real_friends = Friends(user=user_real)
        user_real_friends.save()
    try:
        my_friends = Friends.objects.get(user=request.user)
    except:
        my_friends = Friends(user=request.user)
        my_friends.save()
    
    is_friend = request.user in user_real.friends.users.all() and user_real in request.user.friends.users.all()
    is_requested = request.user in user_real.friend_requests.users.all()

    context = {
        'social_account': social_account,
        'user_real': user_real,
        'departments': departments,
        'empty': len(departments) == 0,
        'name': name,
        'is_friend': is_friend,
        'is_requested': is_requested,
    }
    return render(request, 'user_profile/other_profile.html', context)