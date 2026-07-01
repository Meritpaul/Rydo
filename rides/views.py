from django.shortcuts import render, redirect
from .models import RideRequest


def ride_list(request):

    rides = RideRequest.objects.all().order_by("-id")

    return render(
        request,
        "rides.html",
        {
            "rides": rides
        }
    )


def create_ride(request):

    if request.user.role != "customer":
        return redirect("/driver/dashboard/")

    if request.method == "POST":

        RideRequest.objects.create(
            customer=request.user,
            pickup_location=request.POST.get("pickup"),
            drop_location=request.POST.get("drop"),
            pickup_time=request.POST.get("pickup_time"),
        )

        return redirect("/rides/")

    return render(request, "create_ride.html")