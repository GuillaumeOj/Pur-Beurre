from django.shortcuts import render, redirect, reverse

from product.models import Product
from product.forms import ProductSearchForm


# Create your views here.
def find(request):
    """
    Find the product, the user want to substitute
    """
    if request.method == "POST":
        form = ProductSearchForm(request.POST)
        context = {"product_search_form": form}

        if form.is_valid():
            product = Product.objects.find_product(form.cleaned_data["name"])

            if product:
                substitutes = Product.objects.find_substitute(product.code)
                context["product"] = product
                context["substitutes"] = substitutes

            return render(request, "search/substitutes.html", context=context)
    return redirect(reverse("homepage:index"))
