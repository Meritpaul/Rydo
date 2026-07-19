from django.shortcuts import render

from django.shortcuts import render, redirect
from rides.models import RideRequest
from bookings.models import DriverOffer
from bookings.models import Booking
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import get_user_model


User = get_user_model()


def create_offer(request, ride_id):

    ride = RideRequest.objects.get(id=ride_id)

    if request.method == "POST":

        amount = request.POST.get("amount")

        driver = User.objects.first()

        DriverOffer.objects.create(
            ride=ride,
            driver=driver,
            amount=amount
        )

        return redirect("/rides/")

    return render(
        request,
        "create_offer.html",
        {
            "ride": ride
        }
    )


def view_offers(request, ride_id):

    offers = DriverOffer.objects.filter(
        ride_id=ride_id
    )

    return render(
        request,
        "view_offers.html",
        {
            "offers": offers
        }
    )


def home(request):

    return render(
        request,
        "home.html"
    )


def accept_offer(request, offer_id):

    offer = DriverOffer.objects.get(id=offer_id)

    # Accept selected offer
    offer.status = "accepted"
    offer.save()

    # Reject all other offers for this ride
    DriverOffer.objects.filter(
        ride=offer.ride
    ).exclude(
        id=offer.id
    ).update(status="rejected")

    ride = offer.ride

    # Update ride status
    ride.status = "booked"
    ride.save()

    # Create booking only if it doesn't already exist
    Booking.objects.get_or_create(
        ride=ride,
        defaults={
            "offer": offer,
            "customer": ride.customer,
            "driver": offer.driver,
            "status": "accepted",
        }
    )

    return redirect(f"/offers/{ride.id}/")


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect("/dashboard/")

    return render(
        request,
        "login.html"
    )


def dashboard(request):

    rides = RideRequest.objects.filter(
        customer=request.user
    )

    total_rides = rides.count()

    pending = rides.filter(
        status="pending"
    ).count()

    booked = rides.filter(
        status="booked"
    ).count()

    return render(
        request,
        "dashboard.html",
        {
            "rides": rides.order_by("-id"),
            "total_rides": total_rides,
            "pending": pending,
            "booked": booked,
        },
    )


def driver_dashboard(request):
    
    if request.user.role != "driver":
        return redirect("/dashboard/")

    rides = RideRequest.objects.filter(
        status="pending"
    )

    return render(
        request,
        "driver_dashboard.html",
        {
            "rides": rides
        }
    )