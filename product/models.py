from django.db import models

from django.core.validators import MaxLengthValidator, URLValidator, MinLengthValidator


# Create your models here.
class Category(models.Model):
    """
    Category for a product
    """

    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(1), MaxLengthValidator],
    )

    def __str__(self):
        return self.name


class Store(models.Model):
    """
    Store in which a product is sell
    """

    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(1), MaxLengthValidator],
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Product's brand
    """

    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(1), MaxLengthValidator],
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product from openfoodfact
    """

    code = models.CharField(
        max_length=13,
        unique=True,
        validators=[MinLengthValidator(13), MaxLengthValidator(13)],
    )

    name = models.CharField(
        max_length=100, validators=[MinLengthValidator(1), MaxLengthValidator]
    )

    generic_name = models.CharField(
        blank=True, max_length=100, validators=[MaxLengthValidator]
    )

    quantity = models.CharField(
        blank=True, max_length=50, validators=[MaxLengthValidator]
    )

    ingredients_text = models.TextField(blank=True)

    nutriscore_grade = models.CharField(
        max_length=1, validators=[MinLengthValidator(1), MaxLengthValidator(1)],
    )

    url = models.URLField(
        validators=[MinLengthValidator(1), MaxLengthValidator, URLValidator],
    )

    image_url = models.URLField(blank=True, validators=[MaxLengthValidator, URLValidator])
    image_small_url = models.URLField(
        blank=True, validators=[MaxLengthValidator, URLValidator]
    )

    # Related fields
    categories = models.ManyToManyField(Category)
    stores = models.ManyToManyField(Store)
    brands = models.ManyToManyField(Brand)

    # objects = ProductManager()

    def __str__(self):
        return f"{self.code} - {self.name}"
