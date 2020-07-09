from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Category for a product
    """

    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Store(models.Model):
    """
    Store in which a product is sell
    """

    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Product's brand
    """

    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product from openfoodfact
    """

    code = models.BigIntegerField(unique=True)

    name = models.CharField(max_length=100)

    generic_name = models.CharField(blank=True, max_length=100)

    quantity = models.CharField(blank=True, max_length=50)

    ingredients_text = models.TextField(blank=True)

    nutriscore_grade = models.CharField(blank=True, max_length=250)

    url = models.CharField(max_length=250)

    image_url = models.CharField(blank=True, max_length=250)
    image_small_url = models.CharField(blank=True, max_length=250)

    # Related fields
    categories = models.ManyToManyField(Category)
    stores = models.ManyToManyField(Store)
    brands = models.ManyToManyField(Brand)

    def __str__(self):
        return f"{self.code} - {self.name}"
