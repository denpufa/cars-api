from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=20)
    active =  models.BooleanField(default=True)

