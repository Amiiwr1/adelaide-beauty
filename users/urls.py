from django.urls import path
from rest_framework.authtoken import views

from .views import UserAPIView, SignUpView

app_name = 'users'

urlpatterns = [
    path('auth/', views.obtain_auth_token, name='token'),
    path('api/register/', UserAPIView.as_view(), name='register'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
