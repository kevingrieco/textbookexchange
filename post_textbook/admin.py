from django.contrib import admin
from .models import Textbook, Course, Department

# Register your models here.
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'edition', 'year', 'author', 'department', 'course', 'publisher')

admin.site.register(Textbook, TextbookAdmin)
admin.site.register(Course)
admin.site.register(Department)
