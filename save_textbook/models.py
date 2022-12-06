from django.db import models
from django.contrib.auth.models import User
from post_textbook.models import Textbook

class Favorites(models.Model):
    user = models.OneToOneField(User, related_name='favorites', on_delete=models.CASCADE)
    textbooks = models.ManyToManyField(Textbook)