from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProductSearchForm
from .models import Favorite, Product


def sheet(request, product_code):
    """Display the detail sheet for a product.

    :param product_code: the code for the product to display
    :type product_code: str
    :return: an HttpResponse with a template and context dictionnary
    :rtype: HttpResponse
    """
    product_search_form = ProductSearchForm()
    context = {
        "product_search_form": product_search_form,
    }

    product = Product.objects.get_product_by_code(product_code)
    context["product"] = product

    return render(request, "product/sheet.html", context=context)


@login_required
def save_favorite(request, product_code, substitute_code):
    """Save a substitute in favorites for the current user.

    :param product_code: the code for the substituted product
    :type product_code: str
    :param substitute_code: the code for the substitute
    :type substitute_code: str
    :return: redirect to the previous page
    :rtype: HttpResponseRedirect
    """
    product = Product.objects.get_product_by_code(product_code)
    substitute = Product.objects.get_product_by_code(substitute_code)

    current_user = request.user

    favorite, created = Favorite.objects.get_or_create(
        product=product, substitute=substitute
    )
    if favorite not in current_user.favorites.all():
        current_user.favorites.add(favorite)
        success_message = f"{substitute.name} est sauvegardé dans vos favoris"
        messages.success(request, success_message)
    else:
        error_message = (
            f"{substitute.name} est déjà dans vos favoris pour substituer {product.name}"
        )
        messages.error(request, error_message)

    return redirect(request.META["HTTP_REFERER"])


@login_required
def favorites(request):
    """Display all favorites for the current user.

    :return: an HttpResponse with a template and context dictionnary
    :rtype: HttpResponse
    """
    product_search_form = ProductSearchForm()
    context = {
        "product_search_form": product_search_form,
    }
    favorites = request.user.favorites.order_by("-product")
    context["favorites"] = favorites

    return render(request, "product/favorites.html", context=context)
