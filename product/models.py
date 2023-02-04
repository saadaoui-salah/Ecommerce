from django.db import models
from account.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .managers import *


class Category(models.Model):
    parent     = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name       = models.CharField(max_length=30)
    icon       = models.ImageField(upload_to='categories')
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name       = models.CharField(max_length=20)
    details    = models.TextField()
    price      = models.FloatField()
    stock      = models.IntegerField()
    image      = models.ImageField(upload_to="media/products")
    created_at = models.DateTimeField(auto_now_add=True)
    objects    = ProductManager()

class ProductTracks(models.Model):
    product    = models.OneToOneField(Product, on_delete=models.CASCADE)
    clicks     = models.IntegerField(default=0)
    views      = models.IntegerField(default=0)
    orders     = models.IntegerField(default=0)


class Review(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars      = models.IntegerField(choices=[(1, 1),(2, 2),(3, 3),(4, 4),(5, 5)])
    review     = models.TextField()
    objects    = ReviewManager()


class Cobon(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    code     = models.CharField(max_length=6)
    benifits = models.IntegerField()


class Discount(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    percentage = models.IntegerField()



@receiver(pre_save, sender=Product)
def my_handler(sender, instance, **kwargs):
    if instance.pk:
        ProductTracks.objects.create(product=instance)
