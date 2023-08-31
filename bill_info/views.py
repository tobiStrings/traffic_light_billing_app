from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.decorators import api_view
from .models import BillingInformation
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .serializers import BillInfoSerializer
from rest_framework.response import Response
from .service.billling_info_service import BillingInfoService
from traffic_light.serializers import TraficLightDetailsSerializer

def get_billing_info_by_bill_number(request, bill_number):
    try:
        billing_info = BillingInformation.objects.get(bill_number = bill_number)
        serilizer = BillInfoSerializer(billing_info)
        return JsonResponse(serilizer.data,status=200)
    except ObjectDoesNotExist:
        error_message = {'error':"Billing info with "+bill_number+ " does not exist!"}
        return JsonResponse(error_message, status=404)
    
def get_all_billing_info(request):
      data = BillingInfoService.fetch_all_billing_info()
      if data:
          return JsonResponse(data,status=status.HTTP_200_OK,safe=False)
      
      error_message = {"message":"There is nothing to fetch in the datbase"}
      return JsonResponse(error_message,status=status.HTTP_400_BAD_REQUEST)
  
  
@api_view(['POST'])
def add_billing_info(request):
    if request.method == 'POST':
        data = request.data
        billing_info = BillingInfoService.add_bill_info(data)
        print("Biling info "+str(billing_info))
        if billing_info:
            serilizer = BillInfoSerializer(billing_info)
            return JsonResponse(serilizer.data,status=status.HTTP_201_CREATED)
        else:
            error_message = {"message":"Can't save object because you did not pass a request body"}
            return JsonResponse(error_message,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def verify_if_billed_corretly(request):
#     if request.method == 'POST':
#         data = request.data
#         res = BillingInfoService.verify_if_billed_corretly(data)
#         details_list = list(res.values())  # Convert QuerySet to a list of dictionaries
#         response = {'details': details_list}
#         if res :
#             return JsonResponse(response,status=status.HTTP_200_OK)
#         error_message = {"message":"Can't save object because you did not pass a request body"}
#         return JsonResponse(error_message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verify_if_billed_corretly(request):
    if request.method == 'POST':
        data = request.data
        traffic_light_details = BillingInfoService.verify_if_billed_corretly(data)
        
        if traffic_light_details:
            details_list = []
            
            for detail in traffic_light_details:
                serializer = TraficLightDetailsSerializer(detail)  # Create a serializer instance
                serialized_data = serializer.data  # Get the serialized data
                
                details_list.append(serialized_data)
            det = BillingInfoService.build_response_for_verifying(details_list)
            print("det "+str(det))
            response = {'details': det}
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            error_message = {"message": "Can't retrieve details or no details found"}
            return JsonResponse(error_message, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
