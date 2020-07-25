"""Urls for the homepage app."""
from django.urls import path

from . import views

app_name = "homepage"
urlpatterns = [
    path("", views.index, name="index"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
]
