from django.shortcuts import render, redirect
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

def _recipient_str(user, conversation):
    recipient_user = 'user_a' if conversation.user_a != user else 'user_b'
    recipient_full_name = None
    if recipient_user == 'user_a':
        if conversation.user_a.first_name and conversation.user_a.last_name:
            recipient_full_name = conversation.user_a.first_name + " " + conversation.user_a.last_name
        recipient_username = conversation.user_a.username
    elif recipient_user == 'user_b':
        if conversation.user_b.first_name and conversation.user_b.last_name:
            recipient_full_name = conversation.user_b.first_name + " " + conversation.user_b.last_name
        recipient_username = conversation.user_b.username
    return recipient_username, recipient_full_name

def view_conversation(request, pk):
    sender = request.user
    try:
        conversation = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return redirect('direct_messages:inbox')
    if (conversation.user_a != sender and conversation.user_b != sender):
        return redirect('direct_messages:inbox')
    recipient, full_name = _recipient_str(request.user, conversation)
    context = {
        'full_name': full_name,
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
    conversation.latest = message.time
    conversation.save()
    return redirect('direct_messages:view_conversation', pk=conversation.pk)


def inbox(request):
    conversations = Conversation.objects.filter(user_a=request.user) | Conversation.objects.filter(user_b=request.user)
    context = {
        'conversations': conversations,
    }
    return render(request, 'direct_messages/inbox.html', context)
