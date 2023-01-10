from .views import *
from django.urls import path


urlpatterns = [
    path('signup/', sign_up),
    path('login/', authenticate_user),
    path('settings/', get_settings),
    path('settings/update-password/', update_password),
    path('logout/',log_user_out)
]