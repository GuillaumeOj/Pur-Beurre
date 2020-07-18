from django.urls import path

from . import views

app_name = "product"
urlpatterns = [
    path("sheet/<str:product_code>/", views.sheet, name="sheet"),
]
