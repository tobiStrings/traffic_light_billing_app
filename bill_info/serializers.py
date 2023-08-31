from rest_framework import serializers
from .models import BillingInformation

class BillInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInformation
        fields = ['bill_number','payment_code','number_plate','traffic_light','date']

class BillingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInformation
        fields = '__all__'

class AddBillInfoRequest():
    def __init__(self, bill_number, traffic_light_id, payment_code,number_plate):
        self.bill_number = bill_number
        self.traffic_light_id = traffic_light_id
        self.payment_code = payment_code
        self.number_plate = number_plate
        
class AddBillInfoRequestSerializer(serializers.Serializer):
    bill_number = serializers.CharField()
    traffic_light_id = serializers.IntegerField()
    payment_code = serializers.CharField()
    number_plate = serializers.CharField()