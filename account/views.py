from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from product.models import Order

def sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context=context)
    if request.method == 'POST':
        print(request.FILES)
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['email'].split('@')[0], password=request.POST['password1'])
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)

def authenticate_user(request):
    if request.user == AnonymousUser:
        return redirect('/')
    else:
        if request.method == "GET":
            return render(request, template_name="login.html")
        if request.method == "POST":
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, context={'error': 'User Not Found'}, template_name='login.html')
            else:
                login(request, user)
                try:
                    return redirect(request.get_full_path().split('=')[1])
                except:
                    return redirect('/')

def log_user_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/login/")
def get_profile(request):
    context = {
        'orders_count': Order.objects.filter(user_id=request.user.id).count(),
        'orders': Order.objects.filter(user_id=request.user.id),
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    orders = Order.objects.filter(user__id=request.user.id)
    spent = 0
    if len(orders) > 0:
        prices = list(orders.values_list('product__price'))   
        for price in prices:
            spent += price[0]
    context['spent'] = spent
    
    return render(request, 'profile.html', context)
