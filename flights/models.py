from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.flight_number}: {self.source} to {self.destination}"
    
    def save(self, *args, **kwargs):
        if not self.pk:  # If it's a new flight
            self.available_seats = self.total_seats
        super().save(*args, **kwargs)