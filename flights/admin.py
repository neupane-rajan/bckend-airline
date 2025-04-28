from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'source', 'destination', 'departure_date', 'departure_time', 'available_seats', 'price')
    search_fields = ('flight_number', 'source', 'destination')
    list_filter = ('departure_date', 'source', 'destination')