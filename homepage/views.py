from django.shortcuts import render

from product.forms import ProductSearchForm


def index(request):
    """Landing page."""
    product_search_form = ProductSearchForm()
    context = {"product_search_form": product_search_form}
    return render(request, "homepage/home.html", context=context)


def disclaimer(request):
    """Display the disclaimer."""
    product_search_form = ProductSearchForm()
    context = {"product_search_form": product_search_form}
    return render(request, "homepage/disclaimer.html", context=context)


def trigger_error(request):
    """Only for trigger an error in sentry"""
    division_by_zero = 1 / 0

    return division_by_zero
