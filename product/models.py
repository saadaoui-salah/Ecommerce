from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="media/products")

class Order(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    count       = models.IntegerField()
    date        = models.DateTimeField(auto_now_add=True)

class ShoppingCard(models.Model):
    orders       = models.ManyToManyField(Order)
    phone_number = models.IntegerField()
    adresse      = models.CharField(max_length=100)
    date        = models.DateTimeField(auto_now_add=True)

class HashSessions(models.Model):
    hash_key = models.CharField(max_length=100)
    