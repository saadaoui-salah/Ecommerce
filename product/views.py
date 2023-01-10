from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Review, Discount
from order.models import Order 
from analytics.models import UserTrack
from django.contrib.auth.decorators import login_required


def list_products(request):
    UserTrack.objects.create(
        url='product-list',
        user_agent=request.headers['User-Agent'],
        ip_address=request.headers['Host']
        )
    products = Product.objects.all().get_details()
    context = {
        'products': products, 
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    response = render(request, 'product/product.html', context) 
    return response

def get_product_details(request, id):
    product = Product.objects.filter(id=id).get_details()[0]
    reviews = Review.objects.filter(product__id=id)
    reviews_num = reviews.count()
    star_1 = reviews.get_1_star_percentage()
    star_2 = reviews.get_2_star_percentage()
    star_3 = reviews.get_3_star_percentage()
    star_4 = reviews.get_4_star_percentage()
    star_5 = reviews.get_5_star_percentage()
    reviews_avg = reviews.get_avg_rating()
    sold   = Order.objects.filter(product__id=id).count()
    context = {
        'sold': sold,
        'reviews': reviews,
        'reviews_num': reviews_num,
        'reviews_avg': reviews_avg,
        'star_1': star_1.__round__(),
        'star_2': star_2.__round__(),
        'star_3': star_3.__round__(),
        'star_4': star_4.__round__(),
        'star_5': star_5.__round__(),
        'product': product, 
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
    }
    if request.method == 'POST':
        Review.objects.create(
            product=product,
            user=request.user,
            stars=request.POST['stars'],
            review=request.POST['review']
        )
    return render(request, 'product/product-details.html', context)

@login_required(login_url='/login/')
def list_products_for_seller(request):
    products = Product.objects.filter(user__id=request.user.id)
    context = {
            'products': products, 
            'user': request.user,
            'logged_in': True if request.user.is_authenticated else False,
            'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    return render(request, 'account/seller/products.html')

@login_required(login_url='/login/')
def create_product(request):
    Product.objects.create(

    )
    context = {
            'user': request.user,
            'logged_in': True if request.user.is_authenticated else False,
            'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    return render(request, 'account/seller/.html', context)

@login_required(login_url='/login/')
def update_product(request):
    context = {
            'user': request.user,
            'logged_in': True if request.user.is_authenticated else False,
            'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    return render(request, 'account/seller/.html', context)

@login_required(login_url='/login/')
def delete_product(request):
    context = {
            'user': request.user,
            'logged_in': True if request.user.is_authenticated else False,
            'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    return render(request, 'account/seller/.html', context)



def healthy_check(request):
    return HttpResponse("Server is runing ...")