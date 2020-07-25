from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import redirect, render, reverse

from product.forms import ProductSearchForm
from product.models import Product


def auto_find(request):
    """Return products'names for autocompletion."""
    if request.method == "POST":
        form = ProductSearchForm(request.POST)

        products = Product.objects.find_products(form["name"].value())

        products_names = [product.name for product in products]

        products_names = list(set(products_names))
        print(products_names)

        response = {"products_names": products_names}

        return JsonResponse(response)


def find(request):
    """Find the product, the user want to substitute."""
    if request.method == "POST":
        form = ProductSearchForm(request.POST)
        context = {"product_search_form": form}

        if form.is_valid():
            product = Product.objects.find_product(form.cleaned_data["name"])

            if product:
                return redirect(reverse("search:find_substitutes", args=[product.code]))
            else:
                context["product"] = {"name": form.cleaned_data["name"]}

            return render(request, "search/substitutes.html", context=context)
    return redirect(reverse("homepage:index"))


def find_substitutes(request, product_code, page=1):
    form = ProductSearchForm()
    context = {"product_search_form": form}

    product = Product.objects.get(code=product_code)

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
    else:
        context["product"] = {"name": form.cleaned_data["name"]}
    return render(request, "search/substitutes.html", context=context)
