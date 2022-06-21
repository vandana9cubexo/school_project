

# Create your models here.
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField( )
    std = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    describe = models.TextField(default='')

    def __str__(self):
        return self.name