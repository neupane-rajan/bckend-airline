# flights/mock_data.py
import random
import datetime
from dateutil.relativedelta import relativedelta

# Major Indian airports with more options
indian_airports = [
    {"code": "DEL", "name": "Indira Gandhi International", "city": "Delhi", "terminal_count": 3},
    {"code": "BOM", "name": "Chhatrapati Shivaji", "city": "Mumbai", "terminal_count": 2},
    {"code": "MAA", "name": "Chennai International", "city": "Chennai", "terminal_count": 2},
    {"code": "BLR", "name": "Kempegowda International", "city": "Bengaluru", "terminal_count": 2},
    {"code": "HYD", "name": "Rajiv Gandhi International", "city": "Hyderabad", "terminal_count": 1},
    {"code": "CCU", "name": "Netaji Subhas Chandra Bose", "city": "Kolkata", "terminal_count": 2},
    {"code": "GOI", "name": "Dabolim Airport", "city": "Goa", "terminal_count": 1},
    {"code": "AMD", "name": "Sardar Vallabhbhai Patel", "city": "Ahmedabad", "terminal_count": 1},
    {"code": "COK", "name": "Cochin International", "city": "Kochi", "terminal_count": 3},
    {"code": "PNQ", "name": "Pune Airport", "city": "Pune", "terminal_count": 1},
    {"code": "LKO", "name": "Chaudhary Charan Singh", "city": "Lucknow", "terminal_count": 2},
    {"code": "JAI", "name": "Jaipur International", "city": "Jaipur", "terminal_count": 2},
    {"code": "IXC", "name": "Chandigarh Airport", "city": "Chandigarh", "terminal_count": 1},
    {"code": "PAT", "name": "Jay Prakash Narayan", "city": "Patna", "terminal_count": 1},
    {"code": "BBI", "name": "Biju Patnaik", "city": "Bhubaneswar", "terminal_count": 1},
    {"code": "IXZ", "name": "Veer Savarkar International", "city": "Port Blair", "terminal_count": 1},
    {"code": "GAU", "name": "Lokpriya Gopinath Bordoloi", "city": "Guwahati", "terminal_count": 1},
    {"code": "IXB", "name": "Bagdogra Airport", "city": "Siliguri", "terminal_count": 1},
    {"code": "ATQ", "name": "Sri Guru Ram Dass Jee", "city": "Amritsar", "terminal_count": 1},
    {"code": "VGA", "name": "Vijayawada Airport", "city": "Vijayawada", "terminal_count": 1}
]

# Popular international airports
international_airports = [
    {"code": "DXB", "name": "Dubai International", "city": "Dubai", "country": "UAE", "terminal_count": 3},
    {"code": "SIN", "name": "Singapore Changi", "city": "Singapore", "country": "Singapore", "terminal_count": 4},
    {"code": "LHR", "name": "Heathrow", "city": "London", "country": "UK", "terminal_count": 5},
    {"code": "JFK", "name": "John F. Kennedy", "city": "New York", "country": "USA", "terminal_count": 6},
    {"code": "BKK", "name": "Suvarnabhumi", "city": "Bangkok", "country": "Thailand", "terminal_count": 2},
    {"code": "SYD", "name": "Sydney Airport", "city": "Sydney", "country": "Australia", "terminal_count": 3},
    {"code": "HKG", "name": "Hong Kong International", "city": "Hong Kong", "country": "Hong Kong", "terminal_count": 2},
    {"code": "ICN", "name": "Incheon International", "city": "Seoul", "country": "South Korea", "terminal_count": 2},
    {"code": "FRA", "name": "Frankfurt Airport", "city": "Frankfurt", "country": "Germany", "terminal_count": 3},
    {"code": "CDG", "name": "Charles de Gaulle", "city": "Paris", "country": "France", "terminal_count": 3}
]

# Indian and major international airlines with more details
airlines = [
    {"code": "AI", "name": "Air India", "country": "India", "alliance": "Star Alliance"},
    {"code": "UK", "name": "Vistara", "country": "India", "alliance": "None"},
    {"code": "SG", "name": "SpiceJet", "country": "India", "alliance": "None"},
    {"code": "6E", "name": "IndiGo", "country": "India", "alliance": "None"},
    {"code": "G8", "name": "GoAir", "country": "India", "alliance": "None"},
    {"code": "IX", "name": "Air India Express", "country": "India", "alliance": "None"},
    {"code": "EK", "name": "Emirates", "country": "UAE", "alliance": "None"},
    {"code": "SQ", "name": "Singapore Airlines", "country": "Singapore", "alliance": "Star Alliance"},
    {"code": "BA", "name": "British Airways", "country": "UK", "alliance": "Oneworld"},
    {"code": "QR", "name": "Qatar Airways", "country": "Qatar", "alliance": "Oneworld"},
    {"code": "LH", "name": "Lufthansa", "country": "Germany", "alliance": "Star Alliance"},
    {"code": "TG", "name": "Thai Airways", "country": "Thailand", "alliance": "Star Alliance"},
    {"code": "CX", "name": "Cathay Pacific", "country": "Hong Kong", "alliance": "Oneworld"}
]

# Aircraft types with details
aircraft_types = [
    {"model": "Airbus A320", "capacity": 180, "range_km": 6100},
    {"model": "Boeing 737", "capacity": 160, "range_km": 5600},
    {"model": "Airbus A380", "capacity": 525, "range_km": 14800},
    {"model": "Boeing 777", "capacity": 368, "range_km": 15844},
    {"model": "Boeing 787 Dreamliner", "capacity": 242, "range_km": 13530},
    {"model": "Airbus A330", "capacity": 290, "range_km": 11750},
    {"model": "ATR 72", "capacity": 74, "range_km": 1528}
]

# Travel classes with their features
travel_classes = [
    {"name": "Economy", "baggage_allowance_kg": 20, "meal_included": True, "legroom_cm": 76},
    {"name": "Premium Economy", "baggage_allowance_kg": 25, "meal_included": True, "legroom_cm": 84},
    {"name": "Business", "baggage_allowance_kg": 35, "meal_included": True, "legroom_cm": 106},
    {"name": "First", "baggage_allowance_kg": 50, "meal_included": True, "legroom_cm": 152}
]

def generate_flights(count=40, start_date=None):
    """Generate mock flight data with realistic parameters"""
    flights = []
    
    # Use current date if none provided
    if start_date is None:
        start_date = datetime.datetime.now()
    
    # Create a fixed current date for consistent data (using the provided date in the prompt)
    current_date = datetime.datetime(2025, 4, 28, 11, 57, 59)
    
    for i in range(count):
        # Choose domestic or international flight (70% domestic)
        is_domestic = random.random() < 0.7
        
        # Select airports
        if is_domestic:
            # Domestic flight within India
            origin_index = random.randint(0, len(indian_airports) - 1)
            origin = indian_airports[origin_index]
            
            while True:
                destination_index = random.randint(0, len(indian_airports) - 1)
                if destination_index != origin_index:
                    break
                    
            destination = indian_airports[destination_index]
            
            # For domestic flights, mostly Indian carriers
            airline = random.choice([a for a in airlines if a["country"] == "India"])
            aircraft = random.choice(aircraft_types[:3])  # Smaller aircraft for domestic
            travel_class = random.choice(travel_classes[:2])  # Economy or Premium Economy
            
        else:
            # International flight (outbound or inbound)
            is_outbound = random.random() < 0.5
            
            if is_outbound:
                origin = random.choice(indian_airports)
                destination = random.choice(international_airports)
            else:
                origin = random.choice(international_airports)
                destination = random.choice(indian_airports)
            
            # Any airline for international
            airline = random.choice(airlines)
            aircraft = random.choice(aircraft_types)  # Any aircraft type
            travel_class = random.choice(travel_classes)  # Any class
        
        # Generate flight dates (within next 60 days from current_date)
        days_ahead = random.randint(1, 60)
        departure_date = current_date + datetime.timedelta(days=days_ahead)
        
        # Set departure time to a reasonable hour (5 AM to 11 PM)
        departure_hour = random.randint(5, 23)
        departure_minute = random.choice([0, 15, 30, 45])
        departure_date = departure_date.replace(hour=departure_hour, minute=departure_minute)
        
        # Flight duration based on domestic/international
        if is_domestic:
            duration_hours = random.uniform(1.0, 3.0)
        else:
            duration_hours = random.uniform(3.0, 12.0)
        
        # Calculate arrival time
        hours = int(duration_hours)
        minutes = int((duration_hours - hours) * 60)
        arrival_date = departure_date + datetime.timedelta(hours=hours, minutes=minutes)
        
        # Price based on class, domestic/international, and random factors
        base_price = 3000 if is_domestic else 20000
        class_multiplier = {
            "Economy": 1.0,
            "Premium Economy": 1.5,
            "Business": 2.5,
            "First": 5.0
        }
        
        price = base_price * class_multiplier[travel_class["name"]] * random.uniform(0.8, 1.2)
        price = round(price / 100) * 100  # Round to nearest hundred
        
        # Generate a realistic flight number
        flight_number = f"{airline['code']}{random.randint(100, 999)}"
        
        # Available seats (based on capacity and randomness)
        max_capacity = aircraft["capacity"]
        seats_available = int(max_capacity * random.uniform(0.05, 0.5))
        
        # Terminal information
        origin_terminal = random.randint(1, origin.get("terminal_count", 1))
        destination_terminal = random.randint(1, destination.get("terminal_count", 1))
        
        # Create flight object
        flight = {
            "id": i + 1,
            "flight_number": flight_number,
            "airline": airline["name"],
            "airline_code": airline["code"],
            "alliance": airline["alliance"],
            "origin": origin["city"],
            "origin_code": origin["code"],
            "origin_terminal": origin_terminal,
            "destination": destination["city"],
            "destination_code": destination["code"],
            "destination_terminal": destination_terminal,
            "departure_time": departure_date.isoformat(),
            "arrival_time": arrival_date.isoformat(),
            "duration_hours": round(duration_hours, 2),
            "aircraft": aircraft["model"],
            "travel_class": travel_class["name"],
            "baggage_allowance": f"{travel_class['baggage_allowance_kg']}kg",
            "price": price,
            "seats_available": seats_available,
            "is_domestic": is_domestic,
            "meal_included": travel_class["meal_included"],
            "has_wifi": random.choice([True, False]),
            "has_entertainment": random.random() < 0.8,  # 80% have entertainment
            "refundable": random.random() < 0.3,  # 30% are refundable
        }
        
        flights.append(flight)
    
    return flights

# Generate mock flights
mock_flights = generate_flights()

# Example function to search flights
def search_flights(origin=None, destination=None, date=None, passengers=1):
    results = []
    
    for flight in mock_flights:
        matches = True
        
        if origin and flight["origin_code"] != origin and flight["origin"] != origin:
            matches = False
        
        if destination and flight["destination_code"] != destination and flight["destination"] != destination:
            matches = False
            
        if date:
            flight_date = flight["departure_time"].split("T")[0]
            if flight_date != date:
                matches = False
        
        if matches and flight["seats_available"] >= passengers:
            results.append(flight)
    
    return results

# Get all Indian destinations
def get_indian_destinations():
    return [{"code": airport["code"], "city": airport["city"], "name": airport["name"]} for airport in indian_airports]

# Get all international destinations
def get_international_destinations():
    return [{"code": airport["code"], "city": airport["city"], "country": airport["country"], "name": airport["name"]} for airport in international_airports]

# Get all airlines
def get_airlines():
    return airlines