from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser

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
                    return redirect('/home/')

def get_profile(request):
    print(request.user.image)
    return render(request, 'profile.html', {'image': request.user.image if request.user != AnonymousUser else ''})
