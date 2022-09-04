from django.contrib import admin
from .models import Product, Order, ShoppingCard


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ShoppingCard)
