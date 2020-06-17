"""
Views for the homepage
"""
from django.shortcuts import render


def index(request):
    """
    Landing page
    """
    return render(request, "homepage/home.html")
