from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from post_textbook.models import Textbook
from django.contrib.auth import get_user_model


User = get_user_model()
users = User.objects.all()
# Create your views here.

def get_user_textbooks(user):
    textbooks = user.textbooks.all()
    departments = {}
    for textbook in textbooks:
        if not textbook.department in departments:
            departments[textbook.department] = {textbook.course: []}
        departments[textbook.department][textbook.course].append(textbook)
    return departments

def profile(request):
    social_account = SocialAccount.objects.filter(user=request.user)
    departments = get_user_textbooks(request.user)
    context = {
        'social_account': social_account,
        'departments': departments,
        'empty': len(departments) == 0,
    }
    return render(request, 'user_profile/profile.html', context)

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
    context = {
        'social_account': social_account,
        'user_real': user_real,
        'departments': departments,
        'empty': len(departments) == 0,
        'name': name,
    }
    return render(request, 'user_profile/other_profile.html', context)