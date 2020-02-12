from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from .services import UserServices


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'mobile_number')

    def validate_email(self, value):
        if UserServices.email_exists(value):
            raise ValidationError(_("This email already exists !"))
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
