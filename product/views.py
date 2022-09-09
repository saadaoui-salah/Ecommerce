from django.http import HttpResponse
from django.shortcuts import render
from .models import HashSessions, Product, Order, ShoppingCard
import hashlib
import datetime
import json


def createHash():
    hash = hashlib.sha1()
    now = str(datetime.datetime.now().timestamp())
    hash.update(now.encode())
    return  hash.hexdigest()[:-10]

def create_order(request):
    if request.method == 'POST':
        product = Product.objects.filter(id=request.POST['id'])
        order = Order.objects.create(product=product, count=1)
    pass



def list_products(request):
    products = Product.objects.all()
    context = {'products': products}
    response = render(request, 'product.html', context) 
    response.set_cookie('data', 'none')
    if request.COOKIES.get('hash_key') == None: 
        hash_key = createHash()
        print(hash_key)
        response.set_cookie('hash_key', hash_key)
        HashSessions.objects.create(hash_key=hash_key)
        return response
    return response


def list_orders(request):
    # filter orders
    products = Product.objects.filter(id__in=request.COOKIES.get('product_ids'))
    context = {"products": products}
    return render(request, 'order.html', context)


def create_card(request):
    if request.method == 'POST':
        orders = Order.objects.filter(id=request.POST['id'])
        card = ShoppingCard.objects.create(product=orders, count=1)
    pass

def healthy_check(request):
    return HttpResponse("Server is runing ...")