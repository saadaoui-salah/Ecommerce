from .views import sign_up, authenticate_user, get_profile
from django.urls import path


urlpatterns = [
    path('signup/', sign_up),
    path('login/', authenticate_user),
    path('profile/', get_profile)
]