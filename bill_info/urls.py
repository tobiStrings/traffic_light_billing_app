from django.urls import path
from . import views

urlpatterns = [
    path('billing/<str:bill_number>/', views.get_billing_info_by_bill_number, name='get-billing'),
    path('add/', views.add_billing_info, name='add-bill'),
    path('fetch-all/',views.get_all_billing_info,name='get-all'),
    path('verify-bill/',views.verify_if_billed_corretly,name='verify-bill')
]