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
    data = request.COOKIES.get('data')
    print(data)
    splitted_data = data.split(',')
    data = [] 
    for item in splitted_data:
        product_data = {
            'product': Product.objects.filter(id=int(item.split(':')[0])).get(),
            'count'  : int(item.split(':')[1])
        }
        data.append(product_data)
    
    context = {"data": data}
    return render(request, 'order.html', context)


def create_card(request):
    if request.method == 'POST':
        orders = Order.objects.filter(id=request.POST['id'])
        card = ShoppingCard.objects.create(product=orders, count=1)
    pass

def healthy_check(request):
    return HttpResponse("Server is runing ...")