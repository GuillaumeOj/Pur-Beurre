from django.shortcuts import render, redirect, reverse

from product.models import Product


# Create your views here.
def find(request):
    """
    Find the product, the user want to substitute
    """
    if request.method == "POST":
        data = request.POST

        if data.get("name"):
            product = Product.objects.find_product(data.get("name"))

            if product:
                substitutes = Product.objects.find_substitute(product.code)
                context = {"product": product, "substitutes": substitutes}
            else:
                context = {}

            return render(request, "search/substitutes.html", context=context)
    return redirect(reverse("homepage:index"))
