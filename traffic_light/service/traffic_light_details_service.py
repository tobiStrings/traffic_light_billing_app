from ..models import TrafficLight,TraficLightDetails
from ..exceptions.exceptions import TrafficLightIdIsInvalid,TrafficLightException
import datetime
from ..serializers import TraficLightDetailsSerializer
from .traffic_light_service import TrafficLightService
class TraficLightDetailsService:
    @staticmethod
    def add_trafic_light_details(data):
        if data:
            traffic_light_details = TrafficLightService.get_trafic_light_by_id(data['traffic_light_id'])
            traf_details_obj = {
                'traffic_light':traffic_light_details.pk,
                'current_color':data['current_color'],
                'current_date':data['current_date']
            }

            serializer = TraficLightDetailsSerializer(data=traf_details_obj)
            
            if serializer.is_valid():
                traffic_light_details = serializer.save()
                print("Traffic light details saved:", traffic_light_details)
                return traffic_light_details
            else:
                print("Serializer errors:", serializer.errors)
                return None
        else:
            raise TrafficLightException("Data cannot be null")
        
        
    @staticmethod
    def get_details_by_traffic_light_id_and_date(traffic_light_id, current_date):
        res =  TraficLightDetails.objects.filter(traffic_light_id=traffic_light_id, current_date=current_date)
        print("response here "+str(res))
        return res