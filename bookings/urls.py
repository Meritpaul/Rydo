from django.urls import path

from .views import (
    booking_details,
    start_ride,
)


urlpatterns = [

    path(
        "<int:booking_id>/",
        booking_details,
        name="booking_details"
    ),
    
    path(
        "<int:booking_id>/start/",
        start_ride,
        name="start_ride"
    ),

]