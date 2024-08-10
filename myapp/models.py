from django.db import models


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    power = models.CharField(max_length=100)
    extinction = models.CharField(max_length=100)


def __str__(self):
    return self.Name
