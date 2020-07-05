from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserRegistrationForm


class CustomLoginView(SuccessMessageMixin, LoginView):
    success_url = "homepage:index"
    success_message = "Bonjour %(username)s !"


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    success_url = "homepage:index"
    success_message = "À bientôt !"


def registration(request):
    """
    Register a user
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            if first_name:
                success_message = f"Bienvenue parmis nous {first_name} !"
            else:
                success_message = f"Bienvenue parmis nous {username} !"
            messages.success(request, success_message)
            return redirect(reverse("homepage:index"))
    else:
        form = UserRegistrationForm()
    return render(request, "user/registration.html", {"form": form})


@login_required
def account(request):
    """
    User account details
    """
    return render(request, "user/account.html")
