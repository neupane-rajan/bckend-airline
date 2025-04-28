from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from users.permissions import IsOwnerOrAdmin

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    
    def get_queryset(self):
        """
        Admin users can see all bookings.
        Regular users can only see their own bookings.
        """
        user = self.request.user
        if user.userprofile.role == 'admin':
            return Booking.objects.all()
        return Booking.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        booking = self.get_object()
        # Don't allow updating anything except status
        serializer = self.get_serializer(booking, data={'status': request.data.get('status', booking.status)}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        # If booking is cancelled, increase available seats
        if request.data.get('status') == 'cancelled' and booking.status != 'cancelled':
            flight = booking.flight
            flight.available_seats += 1
            flight.save()
        
        return Response(serializer.data)