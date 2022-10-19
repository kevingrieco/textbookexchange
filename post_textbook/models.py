from django.db import models

# Create your models here.
class Textbook(models.Model):

    department = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    edition = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title}, Edition {self.edition} ({self.year}) -- {self.author}"
