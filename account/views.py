from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from order.models import Order
from account.models import User


def sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'account/signup.html', context=context)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['email'].split('@')[0], password=request.POST['password1'])
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'account/signup.html', context={'errors': form.errors})

def authenticate_user(request):
    if request.user == AnonymousUser:
        return redirect('/')
    else:
        if request.method == "GET":
            return render(request, template_name="account/login.html")
        if request.method == "POST":
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, context={'error': 'User Not Found'}, template_name='account/login.html')
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
def get_settings(request):
    if request.method == 'POST':
        user = User.objects.filter(id=request.user.id).select_for_update()
        user.update(
            first_name=request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            address = request.POST['address'],
            phone_number = request.POST['phone_number']
        )
    context = {
        'user': request.user,
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    return render(request, 'account/settings.html', context)


@login_required(login_url="/login/")
def update_password(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        if request.POST['password'] == request.POST['password2']:
            user.set_password(request.POST['password'])        
            user.save()
    context = {
        'user': request.user,
        'logged_in': True if request.user.is_authenticated else False,
        'image': request.user and request.user.image if request.user.is_authenticated else ''
        }
    return render(request, 'account/change_password.html', context)