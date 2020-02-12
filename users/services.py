from .models import CustomUser


class UserServices(object):
    @staticmethod
    def email_exists(email):
        return CustomUser.objects.filter(email=email)
