from django.urls import path

from .views import (
    booking_details,
    start_ride,
    complete_ride,
    cancel_ride,
    my_rides,
    my_trips,
    earnings,
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

    path(
        "<int:booking_id>/complete/",
        complete_ride,
        name="complete_ride"
    ),

    path(
        "my-rides/",
        my_rides,
        name="my_rides"
    ),

    path(
        "my-trips/",
        my_trips,
        name="my_trips"
    ),

    path(
        "earnings/",
        earnings,
        name="earnings",
    ),

    path(
        "<int:booking_id>/cancel/",
        cancel_ride,
        name="cancel_ride",
    ),

]
