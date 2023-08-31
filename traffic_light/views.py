from django.shortcuts import render
from rest_framework.decorators import api_view
from .service.traffic_light_service import TrafficLightService
from .serializers import TrafficLightSerializer,TraficLightDetailsSerializer
from django.http import JsonResponse
from rest_framework import generics,status
from .service.traffic_light_details_service import TraficLightDetailsService

@api_view(['POST'])
def add_traffic_light(request):
    if request.method == 'POST':
        data = request.data        
        traffic_light = TrafficLightService.add_trafic_light(data)

        if traffic_light:
            serializer = TrafficLightSerializer(traffic_light)
            
            print("Serilizer data ", serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
        print("Serializer errors:", serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def add_traffic_light_details(request):
    if request.method == 'POST':
        data = request.data        
        traffic_light_details = TraficLightDetailsService.add_trafic_light_details(data)

        if traffic_light_details:
            serializer = TraficLightDetailsSerializer(traffic_light_details)
            
            print("Serilizer data ", serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
        print("Serializer errors:", serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
