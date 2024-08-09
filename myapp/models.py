from django.db import models


# Create your models here.
class Animal(models.Model):
    Name = models.CharField(max_length=100)
    Weight = models.IntegerField()
    Power = models.CharField(max_length=100)
    Extinction = models.CharField(max_length=100)


def __str__(self):
    return self.Name
