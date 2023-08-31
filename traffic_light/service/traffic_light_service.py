from ..models import TrafficLight
from ..exceptions.exceptions import TrafficLightIdIsInvalid,TrafficLightException
import datetime
from ..serializers import TrafficLightSerializer

class TrafficLightService():
    @staticmethod
    def get_trafic_light_by_id(traffic_light_id):
        if not traffic_light_id:
            raise TrafficLightIdIsInvalid()
        try:
            traffic_light = TrafficLight.objects.get(id=traffic_light_id)
            print(f'traffic_light here {traffic_light}')
            return traffic_light
        except TrafficLight.DoesNotExist: raise TrafficLightException()
    
    @staticmethod
    def add_trafic_light(data):
        if data:
            traf_obj = {
                'location': data['location'],
                'date': TrafficLightService.default_future_date()
            }

            serializer = TrafficLightSerializer(data=traf_obj)
            
            if serializer.is_valid():
                traffic_light = serializer.save()
                print("Traffic light saved:", traffic_light)
                return traffic_light
            else:
                print("Serializer errors:", serializer.errors)
                return None
        else:
            raise TrafficLightException("Data cannot be null")
        
    @staticmethod
    def get_traffic_lights_by_location(location):
        return TrafficLight.objects.filter(location=location)
    
    @staticmethod
    def default_future_date():
        return datetime.datetime.now() + datetime.timedelta(days=7)