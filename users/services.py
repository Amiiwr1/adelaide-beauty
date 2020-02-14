from .models import CustomUser
from django.contrib.auth.hashers import make_password


class UserServices(object):
    @staticmethod
    def email_exists(email):
        return CustomUser.objects.filter(email=email)

    @staticmethod
    def username_password_match(username, password):
        user = CustomUser.objects.get(username=username)
        password_match = user.check_password(password)
        if user and password_match:
            return True
        return False
