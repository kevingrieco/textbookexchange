from django.db import models
from django.contrib.auth.models import User

class Friends(models.Model):
    user = models.OneToOneField(User, related_name='friends', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='friends_list')

class FriendRequests(models.Model):
    user = models.OneToOneField(User, related_name='friend_requests', on_delete=models.CASCADE)
    users = models.ManyToManyField(User)