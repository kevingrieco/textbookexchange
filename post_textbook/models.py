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
    year = models.IntegerField(max_length=4)

    def __str__(self):
        edp = 'st'
        if self.edition % 10 == 1:
            edp == 'st'
        elif self.edition % 10 == 2:
            edp = 'nd'
        elif self.edition % 10 == 3:
            edp = 'rd'
        else:
            edp = 'th'
        
        return f"{self.title},{self.edition}{edp} Edition  ({self.year}) -- {self.author}"
