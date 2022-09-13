from .views import create_card, healthy_check, list_products
from django.urls import path

urlpatterns = [
    path('',list_products),
    path('create-order/<int:id>',create_card),
    path('healthy/', healthy_check)
] 