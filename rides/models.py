from django.db import models
from django.conf import settings

class RideRequest(models.Model):

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    pickup_location = models.CharField(
        max_length=255
    )

    drop_location = models.CharField(
        max_length=255
    )

    pickup_time = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )