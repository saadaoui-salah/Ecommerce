from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Order, ShoppingCart
from analytics.models import UserTrack
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def order_details(request, id):
    product = Product.objects.filter(id=id).get()
    UserTrack.objects.create(
        url='create-order',
        user_agent=request.headers['User-Agent'],
        ip_address=request.headers['Host']
    )
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            product=product,
            count=1
            )
        return redirect('/')
    else:
        context = {
            'product': product, 
            'user': request.user,
            'logged_in': True if request.user.is_authenticated else False,
            'image': request.user and request.user.image if request.user.is_authenticated else ''
            }
        
        return render(request, 'product/order.html', context)

@login_required(login_url='/login/')
def add_to_card(request, id):
#    cart = ShoppingCart.objects.filter(orders__user__id=request.user.id, status='PENDING')
#    product = Product.objects.filter(id=id).get()
#    if len(cart) == 0:
#        cart = ShoppingCart.objects.create()
#        cart.orders.set([order])
#    else:
#        if not order in cart.orders:
#            cart.orders.set([cart.orders, order])
    return redirect('/')

def list_products(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(user__id=request.user.id)
    UserTrack.objects.create(
        url='product-list',
        user_agent=request.headers['User-Agent'],
        ip_address=request.headers['Host']
        )
    products = Product.objects.all()
    context = {
        'products': products, 
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    response = render(request, 'product/product.html', context) 
    return response

def get_product_details(request, id):
    product = Product.objects.get(pk=id)
    context = {
        'product': product, 
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
    }
    return render(request, 'product/product-details.html', context)

def healthy_check(request):
    return HttpResponse("Server is runing ...")