from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.authtoken import views

from .views.web import SignInView, SignUpView
from .views.api import RegisterAPIView, LoginAPIView

app_name = 'users'

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='sign-up'),
    path('login/', SignInView.as_view(), name='sign-in'),
    path('logout/', LogoutView.as_view(), name='sign-out'),
]
