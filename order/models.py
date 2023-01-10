from django.db import models
from account.models import User
from product.models import Product



class Order(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    count        = models.IntegerField() 
    created_at   = models.DateTimeField(auto_now_add=True)

class ShoppingCart(models.Model):
    
    Choices = [
        ('PENDING','PENDING'),
        ('SUBMITTED','SUBMITTED'),
    ]
    
    orders       = models.ManyToManyField(Order)       
    status       = models.CharField(choices=Choices, default='PENDING', max_length=10)
    created_at   = models.DateTimeField(auto_now_add=True)

