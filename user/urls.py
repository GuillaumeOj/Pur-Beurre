"""
Urls for the user app
"""
from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
]
