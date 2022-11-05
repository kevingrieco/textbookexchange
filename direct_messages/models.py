from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.



class Conversation(models.Model):
    unread = models.BooleanField(default=False)
    user_a = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_b_messages")
    user_b = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_a_messages")
    latest = models.DateTimeField(default=datetime.now, blank=True)

    def get_recipient(self, current_user):
        if self.user_a == current_user:
            recipient = self.user_b
        else:
            recipient = self.user_a
        return recipient

class Message(models.Model):

    time = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_messages")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
