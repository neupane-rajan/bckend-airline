from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'flight', 'seat_number', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'flight__flight_number', 'seat_number')