"""
Generic views
"""
from django.shortcuts import render


def index(request):
    """
    Landing page
    """
    return render(request, "generic/home.html")
