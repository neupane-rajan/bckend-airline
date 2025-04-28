from django.db import models
from django.contrib.auth.models import User
from flights.models import Flight

class Booking(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    seat_number = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    
    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number} - {self.seat_number}"
    
    class Meta:
        unique_together = ('flight', 'seat_number')