from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer,BookingListSerializer
from datetime import date

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte = date.today())
    serializer_class = BookingListSerializer