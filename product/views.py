from multiprocessing import context
from django.shortcuts import render
from .models import Product, Order, ShoppingCard


def create_order(request):
    if request.method == 'POST':
        product = Product.objects.filter(id=request.POST['id'])
        order = Order.objects.create(product=product, count=1)
    pass


def list_orders(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)


def list_orders(request):
    # filter orders
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, 'order.html', context)


def create_card(request):
    if request.method == 'POST':
        orders = Order.objects.filter(id=request.POST['id'])
        card = ShoppingCard.objects.create(product=orders, count=1)
    pass