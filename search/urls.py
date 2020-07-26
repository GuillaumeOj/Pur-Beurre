from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.find, name="find"),
    path("auto_find/", views.auto_find, name="auto_find"),
    path("<str:product_code>/", views.find_substitutes, name="find_substitutes"),
    path(
        "<str:product_code>/<str:page>/", views.find_substitutes, name="find_substitutes"
    ),
]
