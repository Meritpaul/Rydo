from django.db import models
from django.conf import settings


class Vehicle(models.Model):

    driver = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    color = models.CharField(max_length=50)

    registration_number = models.CharField(
        max_length=100,
        unique=True
    )

    seats = models.PositiveIntegerField(default=4)

    has_ac = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"