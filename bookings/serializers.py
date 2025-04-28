from rest_framework import serializers
from .models import Booking
from flights.serializers import FlightSerializer
from flights.models import Flight

class BookingSerializer(serializers.ModelSerializer):
    flight_details = FlightSerializer(source='flight', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'user', 'flight', 'flight_details', 'seat_number', 'booking_date', 'status']
        read_only_fields = ['user', 'booking_date']
    
    def create(self, validated_data):
        # Decrease available seats when a booking is made
        flight = validated_data['flight']
        if flight.available_seats <= 0:
            raise serializers.ValidationError("No seats available on this flight")
        
        flight.available_seats -= 1
        flight.save()
        
        return super().create(validated_data)