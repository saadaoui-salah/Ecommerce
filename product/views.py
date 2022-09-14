from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Order
from .forms import ProductForm


def create_order(request, id):
    if request.method == 'POST':
        product = Product.objects.filter(id=id)
        context = {'product': product} 
        print(request.POST)
        return render(request, 'product.html', context)
    product = Product.objects.first()
    print(product)
    context = {'product': product, 'form': ProductForm}
    return render(request, 'order.html', context)


def list_products(request):
    products = Product.objects.all()
    context = {'products': products}
    response = render(request, 'product.html', context) 
    return response


def healthy_check(request):
    return HttpResponse("Server is runing ...")