from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Order


def create_order(request):
    if request.method == 'POST':
        product = Product.objects.filter(id=request.POST['id'])
        order = Order.objects.create(product=product, count=1)
    pass



def list_products(request):
    products = Product.objects.all()
    context = {'products': products}
    response = render(request, 'product.html', context) 
    return response


def create_card(request):
    if request.method == 'POST':
        orders = Order.objects.filter(id=request.POST['id'])
        card = Order.objects.create(product=orders, count=1)
    pass

def healthy_check(request):
    return HttpResponse("Server is runing ...")