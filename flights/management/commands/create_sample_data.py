from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile
from flights.models import Flight
from datetime import datetime, timedelta, time
import random

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Create admin user if not exists
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='adminpassword',
                is_staff=True,
                is_superuser=True
            )
            admin_user.userprofile.role = 'admin'
            admin_user.userprofile.save()
            self.stdout.write(self.style.SUCCESS('Admin user created'))
        
        # Create regular user if not exists
        if not User.objects.filter(username='passenger').exists():
            passenger = User.objects.create_user(
                username='passenger',
                email='passenger@example.com',
                password='passengerpassword'
            )
            passenger.userprofile.role = 'passenger'
            passenger.userprofile.save()
            self.stdout.write(self.style.SUCCESS('Passenger user created'))
        
        # Create sample flights
        if Flight.objects.count() == 0:
            cities = [
                'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
                'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Francisco',
                'Seattle', 'Denver', 'Miami', 'Atlanta', 'Boston', 'Washington DC'
            ]
            
            # Create flights for the next 30 days
            today = datetime.now().date()
            
            for i in range(30):
                flight_date = today + timedelta(days=i)
                
                # Create 5 random flights per day
                for _ in range(5):
                    source = random.choice(cities)
                    destination = random.choice([city for city in cities if city != source])
                    
                    # Random departure time
                    departure_hour = random.randint(6, 22)
                    departure_minute = random.choice([0, 15, 30, 45])
                    departure_time = time(departure_hour, departure_minute)
                    
                    # Calculate flight duration (1-5 hours)
                    flight_duration = timedelta(hours=random.randint(1, 5))
                    
                    # Calculate arrival
                    departure_datetime = datetime.combine(flight_date, departure_time)
                    arrival_datetime = departure_datetime + flight_duration
                    arrival_date = arrival_datetime.date()
                    arrival_time = arrival_datetime.time()
                    
                    # Random flight number (e.g., AA123, DL456)
                    airline_codes = ['AA', 'DL', 'UA', 'SW', 'JB', 'AS', 'NK', 'F9']
                    flight_number = f"{random.choice(airline_codes)}{random.randint(100, 999)}"
                    
                    # Random seat count and price
                    total_seats = random.choice([120, 150, 180, 200, 220])
                    price = round(random.uniform(99.99, 599.99), 2)
                    
                    Flight.objects.create(
                        flight_number=flight_number,
                        source=source,
                        destination=destination,
                        departure_date=flight_date,
                        departure_time=departure_time,
                        arrival_date=arrival_date,
                        arrival_time=arrival_time,
                        total_seats=total_seats,
                        available_seats=total_seats,
                        price=price
                    )
            
            self.stdout.write(self.style.SUCCESS(f'Created {30 * 5} sample flights'))
        else:
            self.stdout.write(self.style.WARNING('Flights already exist, skipping creation'))
        
        self.stdout.write(self.style.SUCCESS('Sample data creation completed!'))