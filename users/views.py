from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserRegistrationForm

User = get_user_model()


class CustomLoginView(SuccessMessageMixin, LoginView):
    success_url = "homepage:index"
    success_message = "Bonjour !"


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
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(
                email=email,
                first_name=first_name,
                password=password,
                last_name=last_name,
            )
            user.save()
            success_message = f"Bienvenue parmis nous {first_name} !"
            messages.success(request, success_message)
            return redirect(reverse("homepage:index"))
    else:
        form = UserRegistrationForm()
    return render(request, "users/registration.html", {"form": form})


@login_required
def account(request):
    """
    User account details
    """
    return render(request, "users/account.html")
