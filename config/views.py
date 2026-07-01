from django.shortcuts import render

from django.shortcuts import render, redirect
from rides.models import RideRequest
from bookings.models import DriverOffer
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
    return render(request, "home.html")


def accept_offer(request, offer_id):

    offer = DriverOffer.objects.get(
        id=offer_id
    )

    offer.status = "accepted"
    offer.save()

    ride = offer.ride

    ride.status = "booked"
    ride.save()

    return redirect(
        f"/offers/{ride.id}/"
    )
    
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

            return redirect("/")

    return render(
        request,
        "login.html"
    )