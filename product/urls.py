from .views import  healthy_check, list_products, create_order
from django.urls import path

urlpatterns = [
    path('',list_products),
    path('create-order/<int:id>',create_order),
    path('healthy/', healthy_check)
] 