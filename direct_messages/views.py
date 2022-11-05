from django.shortcuts import render
from django.views import View
from .models import Conversation, Message 
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

def message_user(request):
    recipient = request.POST.get('recipient')
    sender = request.user
    users = User.objects.all()

    if Conversation.objects.filter(user_a=users.filter(username=sender), user_b=users.filter(username=recipient)).exists():
        conversation = Conversation.objects.get(user_a=users.filter(username=sender), user_b=users.filter(username=recipient))
    elif Conversation.objects.filter(user_b=users.filter(username=sender), user_a=users.filter(username=recipient)).exists():
        conversation = Conversation.objects.get(user_b=users.filter(username=sender), user_a=users.filter(username=recipient))
    else:
        conversation = Conversation(user_a=sender, user_b=recipient)
    
        context = {
        'recipient': recipient,
        'sender': sender,
        'conversation': conversation,
    }

    return render(request, 'messages/message_user.html', context)