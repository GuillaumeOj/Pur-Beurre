from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.find, name="find"),
    path(
        "<str:product_code>/<int:page>/", views.find_substitutes, name="find_substitutes"
    ),
]
