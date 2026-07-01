from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from .models import Booking


def booking_details(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    return render(
        request,
        "booking_details.html",
        {
            "booking": booking
        }
    )


def start_ride(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = "started"
    booking.save()

    booking.ride.status = "started"
    booking.ride.save()

    return redirect(
        f"/bookings/{booking.id}/"
    )