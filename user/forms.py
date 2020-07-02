from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["first_name", "last_name", "email"]
