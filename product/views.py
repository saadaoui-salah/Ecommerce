from ipaddress import ip_address
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Order
from analytics.models import UserTrack

def create_order(request, id):
    UserTrack.objects.create(
        url='create-order',
        user_agent=request.headers['User-Agent'],
        ip_address=request.headers['Host']
    )
    if request.method == 'POST':
        product = Product.objects.filter(id=id).get()
        order = Order.objects.create(
            full_name=request.POST['full_name'],
            product=product,
            count=request.POST['count'],
            phone_number=request.POST['phone_number'],
            adresse=request.POST['adresse']
        )
        return redirect('/success/')
    product = Product.objects.filter(id=id).get()
    context = {'product': product}
    return render(request, 'order.html', context)


def list_products(request):
    UserTrack.objects.create(
        url='product-list',
        user_agent=request.headers['User-Agent'],
        ip_address=request.headers['Host']
        )
    products = Product.objects.all()
    context = {'products': products}
    response = render(request, 'product.html', context) 
    return response

def order_created(request):
    return render(request, 'success.html', {})


def healthy_check(request):
    return HttpResponse("Server is runing ...")