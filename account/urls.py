from .views import sign_up, authenticate_user, get_profile, log_user_out
from django.urls import path


urlpatterns = [
    path('signup/', sign_up),
    path('login/', authenticate_user),
    path('profile/', get_profile),
    path('logout/',log_user_out)
]