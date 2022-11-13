from datetime import datetime
from django.db import models
from django.conf import settings


# Create your models here.



class Conversation(models.Model):
    a_unread = models.BooleanField(default=False)
    b_unread = models.BooleanField(default=False)
    user_a = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_a_messages")
    user_b = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_b_messages")
    latest = models.DateTimeField(default=datetime.now, blank=True)
    

    def get_recipient(self, current_user):
        if self.user_a == current_user:
            recipient = self.user_b
        else:
            recipient = self.user_a
        return recipient

    def get_latest_message(self):
        return self.messages.latest('time')
    
    def __str__(self):
        return f"{self.user_a} & {self.user_b}"

class Message(models.Model):

    time = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_messages")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        return f"{self.content} ({self.time})"
