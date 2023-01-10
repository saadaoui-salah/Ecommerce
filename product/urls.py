from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',list_products),
    path('products/', list_products_for_seller),
    path('product-details/<int:id>', get_product_details), 
    path('healthy/', healthy_check)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)