from django.db import models
from traffic_light.models import TrafficLight
from django.utils import timezone
class BillingInformation(models.Model):
    bill_number = models.CharField(max_length=19)
    traffic_light = models.ForeignKey(TrafficLight, on_delete=models.CASCADE, default=None)
    payment_code = models.CharField(max_length=6)
    number_plate = models.CharField(max_length=8)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return super().__str__()
# Create your models here.
