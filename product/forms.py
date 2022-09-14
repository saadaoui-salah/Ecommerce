from pyexpat import model
from django.forms import ModelForm
from .models import Order


class ProductForm(ModelForm):
    model = Order
    fields = ['product', 'count', 'phone_number', 'adresse']