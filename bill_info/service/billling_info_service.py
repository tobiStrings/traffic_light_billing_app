from traffic_light.service.traffic_light_service import TrafficLightService
from ..models import BillingInformation
from ..serializers import BillInfoSerializer,BillingInfoSerializer,AddBillInfoRequest,AddBillInfoRequestSerializer
from rest_framework.exceptions import ValidationError
from traffic_light.models import TrafficLight
import datetime
from django.core.exceptions import ObjectDoesNotExist
from ..exceptions.exceptions import BillInformationException
from traffic_light.service.traffic_light_details_service import TraficLightDetailsService
from traffic_light.serializers import TrafficLightSerializer
class BillingInfoService():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def add_bill_info(data):
        try:
            traffic_light = TrafficLight.objects.get(id=data['traffic_light_id'])
        except ObjectDoesNotExist:
            print("Traffic Light with provided ID does not exist.")
            return None
        
        dto_dict = {
            "bill_number": data['bill_number'],
            "payment_code": data['payment_code'],
            "number_plate": data['number_plate'],
            "traffic_light": traffic_light.pk,
            "date": BillingInfoService.default_future_date()
        }
        
        serializer = BillInfoSerializer(data=dto_dict)
        
        if serializer.is_valid():
            bill_info = serializer.save()
            print("Bill information saved:", bill_info)
            return bill_info
        else:
            print("Serializer errors:", serializer.errors)
            return None
        
    @staticmethod
    def fetch_all_billing_info():
        billing_info = BillingInformation.objects.all()
        serializer = BillingInfoSerializer(billing_info, many=True)
        return serializer.data
    
    @staticmethod
    def default_future_date():
        return datetime.datetime.now() + datetime.timedelta(days=7)
    
    @staticmethod
    def get_bill_info_by_number_plate(number_plate):
        if not number_plate:
            raise BillInformationException()
        try:
            bill_info = BillingInformation.objects.get(number_plate=number_plate)
            print(f'traffic_light here {bill_info}')
            return bill_info
        except TrafficLight.DoesNotExist: raise BillInformationException()
        
    @staticmethod
    def verify_if_billed_corretly(data):
        search_str_type = data['search_type']
        print("Got here")
        if search_str_type == 'number_plate':
            bill_info = BillingInfoService.get_bill_info_by_number_plate(data['number_plate'])
            traffic_light = TrafficLightService.get_trafic_light_by_id(bill_info.pk)     
            all_traffic_light_at_location = TrafficLightService.get_traffic_lights_by_location(traffic_light.location)
            print("got here too")
            traffic_light_details = []
            for i in all_traffic_light_at_location:
                print("got in here too")
                detail = TraficLightDetailsService.get_details_by_traffic_light_id_and_date(i.pk,bill_info.date)
                print(str(detail))
                for t_light in detail:
                    print("Detail "+ str(t_light.traffic_light))
                    traffic_light_details.append(t_light)
            print("Traffic light details here "+ str(traffic_light_details))
            return traffic_light_details
        
    @staticmethod
    def build_response_for_verifying(details_list):
        print(details_list)
        response = []
        for i in details_list:
            print("I "+str(i))
            print("I "+str(i['traffic_light']))
            t_light = TrafficLightService.get_trafic_light_by_id(i['traffic_light'])
            print("T Light ",t_light)
            print("Traffic light location "+t_light.location)
            obj = {
                'current_light': i['current_color'],  # Access 'current_color' directly from the dictionary
                'location': t_light.location,
                'time_billed': i['current_date'],  # Access 'current_date' directly from the dictionary
            }
            print("Obj "+str(obj))
            response.append(obj)
        print("response "+str(response))
        return response
            
        