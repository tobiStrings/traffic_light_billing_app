from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_traffic_light,name='add-traffic_light'),
    path('add-details/',views.add_traffic_light_details, name='add_traffic_light_details')
]
