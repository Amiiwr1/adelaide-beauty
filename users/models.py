from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    mobile_number = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        error_messages={'unique': _("A user with that mobile number already exists.")},
    )
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password', 'mobile_number']

    def __str__(self):
        return self.email

