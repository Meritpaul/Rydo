from django.shortcuts import render, redirect

from .models import Vehicle


def add_vehicle(request):

    if request.method == "POST":

        Vehicle.objects.update_or_create(

            driver=request.user,

            defaults={

                "brand": request.POST.get("brand"),

                "model": request.POST.get("model"),

                "color": request.POST.get("color"),

                "registration_number": request.POST.get("registration"),

                "seats": request.POST.get("seats"),

                "has_ac": bool(request.POST.get("has_ac")),

            }

        )

        return redirect("/driver/dashboard/")

    return render(
        request,
        "vehicle_form.html"
    )