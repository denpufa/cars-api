from django.db import models
from django.conf import settings


class Car(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=20)
    active =  models.BooleanField(default=True)

    def __str__(self):
        return self.plate_number

 