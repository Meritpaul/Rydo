from django.urls import path

from .views import add_vehicle

urlpatterns = [

    path(
        "add/",
        add_vehicle,
        name="add_vehicle"
    ),

]