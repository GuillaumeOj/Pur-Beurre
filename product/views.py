from django.shortcuts import render

from .models import Product
from .forms import ProductSearchForm


# Create your views here.
def sheet(request, product_code):
    product_search_form = ProductSearchForm()
    context = {
        "product_search_form": product_search_form,
    }

    product = Product.objects.get_product(product_code)
    context["product"] = product

    return render(request, "product/sheet.html", context=context)
