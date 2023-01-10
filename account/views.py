from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"


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
    return render(request, context={}, template_name='profile.html')
