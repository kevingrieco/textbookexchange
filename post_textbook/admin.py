from django.contrib import admin
from .models import Textbook, Course, Department

# Register your models here.
admin.site.register(Textbook)
admin.site.register(Course)
admin.site.register(Department)