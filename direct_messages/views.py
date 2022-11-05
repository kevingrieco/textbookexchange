from django.shortcuts import render, redirect
from django.views import View
from .models import Conversation, Message 
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()
users = User.objects.all()

def _conversation_finder(sender, recipient):
    if Conversation.objects.filter(user_a=users.get(username=sender), user_b=users.get(username=recipient)).exists():
        conversation = Conversation.objects.get(user_a=users.get(username=sender), user_b=users.get(username=recipient))
    elif Conversation.objects.filter(user_b=users.get(username=sender), user_a=users.get(username=recipient)).exists():
        conversation = Conversation.objects.get(user_b=users.get(username=sender), user_a=users.get(username=recipient))
    else:
        conversation = Conversation(user_a=users.get(username=sender), user_b=users.get(username=recipient))
        conversation.save()
    return conversation

def view_conversation(request, pk):
    sender = request.user
    conversation = Conversation.objects.get(pk=pk)
    recipient = conversation.user_a.username if conversation.user_a != request.user else conversation.user_b.username
    context = {
        'recipient': recipient,
        'sender': sender,
        'conversation': conversation,
    }
    return render(request, 'direct_messages/message_user.html', context)

def message_user(request):
    recipient = request.POST.get('recipient')
    sender = request.user
    conversation = _conversation_finder(sender, recipient)
    pk = conversation.pk
    return redirect('direct_messages:view_conversation', pk=pk)
    


def send_message(request):
    sender = request.user
    recipient_name = request.POST.get("recipient")
    recipient = users.get(username=recipient_name)
    conversation = _conversation_finder(sender, recipient)
    content = request.POST.get("content")
    message = Message(
        content=content,
        sender=sender,
        recipient=recipient,
        conversation=conversation,
    )
    message.save()
    return redirect('direct_messages:view_conversation', pk=conversation.pk)


def inbox(request):
    conversations = []
    conversations.append(request.user.user_a_messages)
    conversations.append(request.user.user_b_messages)
    context = {
        'conversations': conversations,
    }
    return render(request, 'direct_messages/inbox.html', context)
