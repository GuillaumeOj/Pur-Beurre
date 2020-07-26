from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import redirect, render, reverse

from product.forms import ProductSearchForm
from product.models import Product

from homepage.custom_http_response import HttpResponseBadRequest


def auto_find(request):
    """Get products' names for the autocompletion."""

    # Avoid reach the view by the GET method
    if request.method == "POST":
        form = ProductSearchForm(request.POST)

        if form.is_valid():
            # Get a list and product and create a list of names
            products = Product.objects.find_products(form["name"].value())
            products_names = [product.name for product in products]
            products_names = list(set(products_names))

            # Create a response as a dict for returning a JsonResponse
            response = {"products_names": products_names}
            return JsonResponse(response)
        else:
            return HttpResponseBadRequest()

    return redirect(reverse("homepage:index"))


def find(request):
    """Find the product, the user want to substitute."""

    # Avoid reach the view by the GET method
    if request.method == "POST":
        product_search_form = ProductSearchForm(request.POST)
        context = {"product_search_form": product_search_form}

        if product_search_form.is_valid():
            # Get the product by using the name
            product = Product.objects.find_product(
                product_search_form.cleaned_data["name"]
            )

            # Redirect to the method find_substitutes if the product exist
            if product:
                return find_substitutes(request, product_code=product.code)
            # Else render the substitute page with no substitutes found
            else:
                context["product"] = {"name": product_search_form.cleaned_data["name"]}
                return render(request, "search/substitutes.html", context=context)

    return redirect(reverse("homepage:index"))


def find_substitutes(request, product_code, page=""):
    """Find substitutes for a product."""

    product_search_form = ProductSearchForm()
    context = {"product_search_form": product_search_form}

    product = Product.objects.get_product(product_code)

    if product:
        context["product"] = product
        substitutes = Product.objects.find_substitutes(product.code)

        if substitutes:
            # Paginate the subsitutes result
            pagination = Paginator(substitutes, 6, orphans=3)
            try:
                context["substitutes"] = pagination.page(page)
            except PageNotAnInteger:
                context["substitutes"] = pagination.page(1)
            except EmptyPage:
                context["substitutes"] = pagination.page(pagination.num_pages)

    return render(request, "search/substitutes.html", context=context)
