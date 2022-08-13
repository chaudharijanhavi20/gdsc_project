from unicodedata import category
from django.db import models

from tkinter import Place
from django.db import models

# Create your models here.
class Events(models.Model):
    category=models.CharField(max_length=50)
    Place=models.CharField(max_length=150)
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return self.name


