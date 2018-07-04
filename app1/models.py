from django.db import models

# Create your models here.

class modue1(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    age = models.IntegerField()