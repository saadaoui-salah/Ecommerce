from .views import SignUpView, authenticate_user, get_profile
from django.urls import path


urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', authenticate_user),
    path('profile/', get_profile)
] 