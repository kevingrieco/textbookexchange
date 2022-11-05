from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model


User = get_user_model()
users = User.objects.all()
# Create your views here.

def profile(request):
    social_account = SocialAccount.objects.filter(user=request.user)
    context = {
        'social_account': social_account
    }
    return render(request, 'user_profile/profile.html', context)

def other_profile(request, username):
    if username == request.user.username:
        return redirect('user_profile:my_profile')
    user_real = users.get(username=username)
    social_account = SocialAccount.objects.filter(user=user_real)
    context = {
        'social_account': social_account,
        'user_real': user_real,
    }
    return render(request, 'user_profile/other_profile.html', context)