from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Order
from analytics.models import UserTrack
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser


@login_required(login_url='/login/')
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
    context = {'product': product, 'image': request.user.image if request.user != AnonymousUser else ''}
    return render(request, 'order.html', context)


def list_products(request):
    UserTrack.objects.create(
        url='product-list',
        user_agent=request.headers['User-Agent'],
        ip_address=request.headers['Host']
        )
    products = Product.objects.all()
    context = {'products': products, 'image': request.user.image if request.user != AnonymousUser else ''}
    response = render(request, 'product.html', context) 
    return response


@login_required(login_url='/login/')
def order_created(request):
    return render(request, 'success.html', {'image': request.user.image if request.user != AnonymousUser else ''})


def healthy_check(request):
    return HttpResponse("Server is runing ...")