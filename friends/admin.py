from django.contrib import admin
from .models import FriendRequests, Friends

# Register your models here.

admin.site.register(Friends)
admin.site.register(FriendRequests)