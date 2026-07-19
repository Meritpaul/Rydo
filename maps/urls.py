from django.urls import path
from . import views

urlpatterns = [
    path(
        "reverse-geocode/",
        views.reverse_geocode,
        name="reverse_geocode",
    ),

    path(
        "route/",
        views.route,
        name="route",
    ),
]
