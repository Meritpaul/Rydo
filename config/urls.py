"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from config.views import (
    home,
    login_view,
    dashboard,
    driver_dashboard,
    create_offer,
    view_offers,
    accept_offer,
)

from rides.views import (
    create_ride,
    ride_list,
)

urlpatterns = [
    path("", home),
    
    path("dashboard/", dashboard),
    path("driver/dashboard/", driver_dashboard),
    path("admin/", admin.site.urls),

    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),

    path("api/rides/", include("rides.urls")),
    path("api/accounts/", include("accounts.urls")),
    path("api/maps/", include("maps.urls")),
    path("vehicles/", include("vehicles.urls")),
    path("bookings/", include("bookings.urls")),
    path("rides/", ride_list),
    path("ride/create/", create_ride),
    path("offer/create/<int:ride_id>/", create_offer),
    path("offers/<int:ride_id>/", view_offers),
    path("offer/accept/<int:offer_id>/", accept_offer),
    path("login/", login_view),
]