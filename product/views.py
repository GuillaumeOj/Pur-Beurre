from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render, reverse

from .forms import ProductSearchForm
from .models import Favorite, Product


# Create your views here.
def sheet(request, product_code):
    product_search_form = ProductSearchForm()
    context = {
        "product_search_form": product_search_form,
    }

    product = Product.objects.get_product(product_code)
    context["product"] = product

    return render(request, "product/sheet.html", context=context)


@login_required
def save_favorite(request, product_code, substitute_code):
    product = Product.objects.get_product(product_code)
    substitute = Product.objects.get_product(substitute_code)

    current_user = request.user

    obj, created = Favorite.objects.get_or_create(product=product, substitute=substitute)
    current_user.favorites.add(obj)
    success_message = f"{substitute.name} est sauvegardé dans vos favoris"
    messages.success(request, success_message)

    return redirect(reverse("search:find_substitutes", args=[product_code, 1]))


@login_required
def favorites(request, page=1):
    product_search_form = ProductSearchForm()
    context = {
        "product_search_form": product_search_form,
    }
    favorites = request.user.favorites.order_by("-product")
    context["favorites"] = favorites

    return render(request, "product/favorites.html", context=context)
