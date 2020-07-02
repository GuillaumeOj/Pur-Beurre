from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from .forms import UserRegistrationForm
from .models import CustomUser


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
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            success_message = f"Bienvenue parmis nous {first_name} !"
            messages.success(request, success_message)
            return redirect(reverse("homepage:index"))
    else:
        form = UserRegistrationForm()
    return render(request, "user/registration.html", {"form": form})
