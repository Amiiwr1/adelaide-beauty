from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import CustomUser
from .services import UserServices


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'mobile_number')

    def validate_email(self, value):
        if UserServices.email_exists(value):
            raise ValidationError(_("This email already exists !"))
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, allow_null=False, allow_blank=False)
    password = serializers.CharField(max_length=128, allow_blank=False, allow_null=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password and UserServices.username_password_match(username=username, password=password):
            return attrs
        raise ValidationError(_("Username or password entered wrong !"))
