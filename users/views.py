from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import SignUpSerializer


class SignUpView(TemplateView):
    template_name = "users/signup.html"


class UserAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password'),
        )
        if user is not None:
            if user.is_active:
                login(request, user)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
