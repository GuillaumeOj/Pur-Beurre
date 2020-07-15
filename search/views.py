from django.shortcuts import render, redirect, reverse
from django.db.models import Count, Q

from product.models import Product


# Create your views here.
def find(request):
    """
    Find the product, the user want to substitute
    """
    if request.method == "POST":
        data = request.POST

        if data.get("name"):
            products = Product.objects.filter(name__icontains=data.get("name"))
            context = {"products": products}
            return render(request, "search/result.html", context=context)
    else:
        return redirect(reverse("homepage:index"))


def substitutes(request, product_code):
    """
    Find substitutes for a product
    """
    if product_code:
        product = Product.objects.get(code=product_code)
        print(type(product_code))
        if product:
            q = Q(categories__in=product.categories.all()) & Q(
                nutriscore_grade__lte=product.nutriscore_grade
            )
            substitutes = (
                Product.objects.annotate(common_categories=Count("categories", filter=q))
                .order_by("-common_categories", "nutriscore_grade")
                .exclude(code=product.code)
            )
            context = {"substitutes": substitutes}
            return render(request, "search/substitutes.html", context=context)
    else:
        return redirect(reverse("homepage:index"))
