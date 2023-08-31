from rest_framework import serializers
from .models import TrafficLight,TraficLightDetails

class TrafficLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficLight
        fields = '__all__'


class TraficLightDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraficLightDetails
        fields = '__all__'


