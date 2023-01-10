from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('create/<int:id>',order_details),
    path('', list_orders),
    path('add-to-cart/<int:id>',add_to_card),
]