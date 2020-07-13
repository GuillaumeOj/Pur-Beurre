from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.find, name="find"),
    path("<int:product_id>/substitutes/", views.substitutes, name="substitutes"),
]
