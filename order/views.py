from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Order, ShoppingCart
from product.models import Product
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
        
        return render(request, 'order/order.html', context)


@login_required(login_url="/login/")
def list_orders(request):
    if request.user.is_seller:
        orders = Order.objects.filter(product__user__id=request.user.id)
    if request.user.is_buyer:    
        orders = Order.objects.filter(user__id=request.user.id)
    context = {
        'user': request.user,
        'orders_count': orders.count(),
        'orders': orders,
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    spent = 0
    if len(orders) > 0:
        prices = list(orders.values_list('product__price'))   
        for price in prices:
            spent += price[0]
    context['spent'] = spent
    return render(request, 'account/seller/orders.html', context)

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
