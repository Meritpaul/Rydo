from rest_framework import generics
from .models import RideRequest
from .serializers import RideRequestSerializer
# rides/views.py

from rest_framework.permissions import IsAuthenticated


class RideCreateView(generics.CreateAPIView):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [IsAuthenticated]
