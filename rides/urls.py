from django.urls import path
from .views import RideCreateView

urlpatterns = [
    path(
        "create/",
        RideCreateView.as_view()
    ),
]