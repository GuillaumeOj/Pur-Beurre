"""
Urls for the user app
"""
from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("registration/", views.registration, name="registration"),
]
