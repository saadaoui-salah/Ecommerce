from .views import create_card, create_order, list_orders, list_products
from django.urls import path

urlpatterns = [
    path('',list_products),
    path('create-order/',create_card),
    path('add-product/',create_order),
    path('card/',list_orders),

] 