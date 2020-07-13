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
            products = Product.objects.filter(name__icontains=data.get("name"))
            context = {"products": products}
            return render(request, "search/result.html", context=context)
    else:
        return redirect(reverse("homepage:index"))


def substitutes(request):
    """
    Find substitutes for a product
    """
    pass
