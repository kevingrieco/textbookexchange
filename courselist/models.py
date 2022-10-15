from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_abbreviation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)


    def __str__(self):
        return self.course_name

class Textbook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.DateField()

    def __str__(self):
        return self.title
