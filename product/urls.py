from .views import order_created, healthy_check, list_products, create_order
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',list_products),
    path('create-order/<int:id>',create_order),
    path('success/', order_created),
    path('healthy/', healthy_check)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)