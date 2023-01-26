from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',list_products),
    path('create-order/<int:id>',order_details),
    path('add-to-cart/<int:id>',add_to_card),
    path('product-details/<int:id>', get_product_details), 
    path('healthy/', healthy_check)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)