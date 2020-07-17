from django.shortcuts import render

from product.forms import ProductSearchForm


def index(request):
    """
    Landing page
    """
    product_search_form = ProductSearchForm()
    context = {"product_search_form": product_search_form}
    return render(request, "homepage/home.html", context=context)
