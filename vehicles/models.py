from django.db import models
from django.conf import settings

class Vehicle(models.Model):

    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    plate_number = models.CharField(max_length=50)

    seats = models.IntegerField()

    def __str__(self):
        return self.plate_number