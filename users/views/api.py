from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import SignUpSerializer, SignInSerializer


class RegisterAPIView(generics.CreateAPIView):
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


class LoginAPIView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data.get('username'),
                password=serializer.validated_data.get('password'),
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
