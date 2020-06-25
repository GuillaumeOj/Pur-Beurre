from django.shortcuts import render


def signup(request):
    """
    Allow user to signup for create an account
    """
    return render(request, "user/signup.html")
