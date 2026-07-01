from django.db import models
from django.conf import settings
from rides.models import RideRequest


class DriverOffer(models.Model):

    ride = models.ForeignKey(
        RideRequest,
        on_delete=models.CASCADE
    )

    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.driver} - {self.amount}"


class Booking(models.Model):

    STATUS_CHOICES = (
        ("accepted", "Accepted"),
        ("started", "Started"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )

    ride = models.OneToOneField(
        RideRequest,
        on_delete=models.CASCADE
    )

    offer = models.OneToOneField(
        DriverOffer,
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_bookings"
    )

    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="driver_bookings"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="accepted"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Booking #{self.id}"