from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(
        _("first name"), max_length=128, blank=False, null=False
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.email
