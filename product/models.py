from django.db import models
from account.models import User

class Category(models.Model):
    parent     = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name       = models.CharField(max_length=30)
    icon       = models.ImageField(upload_to='categories')
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    category   = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name       = models.CharField(max_length=20)
    details    = models.TextField()
    price      = models.FloatField()
    stock      = models.IntegerField()
    image      = models.ImageField(upload_to="media/products")
    created_at = models.DateTimeField(auto_now_add=True)

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

