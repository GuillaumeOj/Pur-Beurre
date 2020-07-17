from django.db import models
from django.db.models import Q, Count
from django.core.validators import MaxLengthValidator, URLValidator, MinLengthValidator

from .category import Category


class ProductManager(models.Manager):
    def get_product(self, product_code):
        """
        Find a specific product
        """
        return self.get_queryset().get(code=product_code)

    def find_product(self, query):
        """
        Find a product TO substitute
        """
        return self.get_queryset().filter(name__icontains=query).first()

    def find_substitute(self, product_code):
        """
        Find a substitute to a specific product
        """
        product = self.get_queryset().get(code=product_code)
        if product:
            q = Q(categories__in=product.categories.all()) & Q(
                nutriscore_grade__lt=product.nutriscore_grade
            )
            substitutes = (
                Product.objects.annotate(common_categories=Count("categories", filter=q))
                .order_by("-common_categories", "nutriscore_grade")
                .exclude(code=product.code)
                .exclude(name=product.name)[:9]
            )
            return substitutes


class Product(models.Model):
    """
    Product from openfoodfact
    """

    # Required fields
    code = models.CharField(
        max_length=13,
        unique=True,
        validators=[MinLengthValidator(13), MaxLengthValidator],
    )

    name = models.CharField(
        max_length=100, validators=[MinLengthValidator(1), MaxLengthValidator]
    )

    nutriscore_grade = models.CharField(
        max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator],
    )

    url = models.URLField(
        validators=[MinLengthValidator(1), MaxLengthValidator, URLValidator],
    )

    # Optionnal fields
    image_url = models.URLField(blank=True, validators=[MaxLengthValidator, URLValidator])
    image_small_url = models.URLField(
        blank=True, validators=[MaxLengthValidator, URLValidator]
    )

    # Related fields
    categories = models.ManyToManyField(Category)

    # Custom product's manager
    objects = ProductManager()

    def __str__(self):
        return f"{self.code} - {self.name}"
