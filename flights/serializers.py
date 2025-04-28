from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'id', 'flight_number', 'source', 'destination', 
            'departure_date', 'departure_time', 'arrival_date', 'arrival_time',
            'total_seats', 'available_seats', 'price'
        ]