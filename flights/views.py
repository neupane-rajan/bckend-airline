from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Flight
from .serializers import FlightSerializer
from users.permissions import IsAdminUser
from .mock_data import mock_flights, search_flights, get_indian_destinations, get_international_destinations

class FlightViewSet(viewsets.ModelViewSet): 
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['source', 'destination', 'departure_date', 'flight_number']
    
    def get_permissions(self):
        """
        Admin users can perform all operations.
        Non-admin users can only list and retrieve flights.
        """
        if self.action in ['list', 'retrieve', 'mock_flights', 'search_mock', 'destinations']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    # Add custom actions for mock data
    @action(detail=False, methods=['get'])
    def mock_flights(self, request):
        """Return all mock flights"""
        return Response(mock_flights)
    
    @action(detail=False, methods=['get'])
    def search_mock(self, request):
        """Search mock flights based on criteria"""
        origin = request.query_params.get('origin', '')
        destination = request.query_params.get('destination', '')
        date = request.query_params.get('date', '')
        passengers = int(request.query_params.get('passengers', 1))
        
        results = search_flights(origin, destination, date, passengers)
        return Response(results)
    
    @action(detail=False, methods=['get'])
    def destinations(self, request):
        """Return all airports/destinations"""
        indian = get_indian_destinations()
        international = get_international_destinations()
        return Response({
            'indian': indian,
            'international': international
        })
    
    @action(detail=True, methods=['get'])
    def mock_detail(self, request, pk=None):
        """Return details for a specific mock flight"""
        try:
            flight_id = int(pk)
            for flight in mock_flights:
                if flight['id'] == flight_id:
                    return Response(flight)
            return Response({'error': 'Flight not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=400)