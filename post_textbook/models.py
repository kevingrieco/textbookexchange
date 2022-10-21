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
        edp = 'st'
        if self.edition % 10 == 1:
            edp == 'st'
        elif self.edition % 10 == 2:
            edp = 'nd'
        elif self.edition % 10 == 3:
            edp = 'rd'
        else:
            edp = 'th'
        
        return f"{self.title}, {self.edition}{edp} Edition  ({self.year}) -- {self.author}"
