from django.core.validators import MaxLengthValidator, MinLengthValidator, URLValidator
from django.db import models
from django.db.models import Count, Q

from .category import Category


class ProductManager(models.Manager):
    """Set custom methods for a product"""

    def get_product(self, product_code):
        """Get a product with the code.

        :param product_code: the code of the product to get
        :type product_code: str
        :return: a query set with the product
        :rtype: QuerySet
        """
        return self.get_queryset().get(code=product_code)

    def find_product(self, name):
        """Get a product with the name.

        Try to get the product by filtering with the exact name, if the query is
        empty, then get the product by filtering with the lookup "__icontains".

        :param name: the name of the product to get
        :type name: str
        :return: a query set with the product
        :rtype: QuerySet
        """
        # Try to find the product with the exact name
        product = self.get_queryset().filter(name=name).first()
        if product:
            return product
        else:
            # Or with name contains the request name
            return self.get_queryset().filter(name__icontains=name).first()

    def find_products(self, name):
        """Get products with the name.

        Get products by filtering with the lookup "__icontains" and limit the results to
        10 products.

        :param name: the name of the product to get
        :type name: str
        :return: a query set with 10 products
        :rtype: QuerySet
        """
        return self.get_queryset().filter(name__icontains=name)[:10]

    def find_substitutes(self, product_code):
        """Get substitutes for a product.

        Get the product by using his code.
        Then get substitutes by counting common categories between each products and the
        substituted product. Keep only products with a nutriscore grade lower than the
        substituted product.
        Return a QuerySet order by common categories count (from largest to smallest) and
        nutriscore grade (from lowest-to-highest).

        :param product_code: the code of the product to get
        :type product_code: str
        :return: a query set with 30 substitutes
        :rtype: QuerySet
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
                .exclude(name=product.name)[:30]
            )
            return substitutes


class Product(models.Model):
    """Model for a product."""

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
    fat_100 = models.FloatField(blank=True, default=0)
    saturated_fat_100 = models.FloatField(blank=True, default=0)
    sugars_100 = models.FloatField(blank=True, default=0)
    salt_100 = models.FloatField(blank=True, default=0)

    # Related fields
    categories = models.ManyToManyField(Category)

    # Custom product's manager
    objects = ProductManager()

    class Meta:
        ordering = ["-name", "code"]

    def __str__(self):
        return f"{self.code} - {self.name}"
