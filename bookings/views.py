from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from django.db.models import Sum

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


def complete_ride(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = "completed"
    booking.save()

    booking.ride.status = "completed"
    booking.ride.save()

    return redirect(
        f"/bookings/{booking.id}/"
    )


def cancel_ride(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    if booking.status != "completed":

        booking.status = "cancelled"
        booking.save()

        booking.ride.status = "cancelled"
        booking.ride.save()

    return redirect(
        f"/bookings/{booking.id}/"
    )


def my_rides(request):

    bookings = Booking.objects.filter(
        customer=request.user
    ).order_by("-id")

    return render(
        request,
        "my_rides.html",
        {
            "bookings": bookings
        }
    )


def my_trips(request):

    bookings = Booking.objects.filter(
        driver=request.user
    ).order_by("-id")

    return render(
        request,
        "my_trips.html",
        {
            "bookings": bookings
        }
    )


def earnings(request):

    bookings = Booking.objects.filter(
        driver=request.user,
        status="completed"
    )

    total_trips = bookings.count()

    total_earnings = (
        bookings.aggregate(
            Sum("offer__amount")
        )["offer__amount__sum"] or 0
    )

    active_trips = Booking.objects.filter(
        driver=request.user,
        status="started"
    ).count()

    return render(
        request,
        "earnings.html",
        {
            "total_trips": total_trips,
            "total_earnings": total_earnings,
            "active_trips": active_trips,
        },
    )
