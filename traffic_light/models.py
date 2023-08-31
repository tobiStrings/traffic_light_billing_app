from django.db import models
from django.utils import timezone

class TrafficLight(models.Model):
    location = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)


class TraficLightDetails(models.Model):
    traffic_light = models.ForeignKey(TrafficLight, on_delete=models.CASCADE, default=None)
    current_color = models.CharField(max_length=5)
    current_date = models.DateTimeField()
    
# Create your models here.
