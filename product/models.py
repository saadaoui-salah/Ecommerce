from django.db import models
from account.models import User

class Product(models.Model):
    name       = models.CharField(max_length=20)
    price      = models.FloatField()
    stock      = models.IntegerField()
    image      = models.ImageField(upload_to="media/products")
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name    = models.CharField(max_length=100)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    count        = models.IntegerField() 
    phone_number = models.IntegerField()
    adresse      = models.CharField(max_length=100)
    created_at   = models.DateTimeField(auto_now_add=True)

