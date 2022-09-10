from .views import create_card, create_order, healthy_check, list_orders, list_products
from django.urls import path

urlpatterns = [
    path('',list_products),
    path('create-order/',create_card),
    path('card/',list_orders),
    path('healthy/', healthy_check)
] 