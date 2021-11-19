from django.db import models
from car.models import Car

class  Client(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    cars = models.ManyToManyField(Car)

