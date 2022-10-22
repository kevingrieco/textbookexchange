from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.name

class Textbook(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="textbooks")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="textbooks")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    edition = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title}, Edition {self.edition} ({self.year}) -- {self.author}"