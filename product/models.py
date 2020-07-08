from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Category for a product
    """

    name = models.CharField(
        verbose_name="Nom de la catégorie",
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        max_length=100,
    )

    def __str__(self):
        return self.name


class Store(models.Model):

    """
    Store in which a product is sell
    """

    name = models.CharField(
        verbose_name="Nom du magasin",
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        max_length=100,
    )

    def __str__(self):
        return self.name


class Brand(models.Model):

    """
    Product's brand
    """

    name = models.CharField(
        verbose_name="Marque du produit",
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        max_length=100,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product from openfoodfact
    """

    code = models.BigIntegerField(
        verbose_name="Code barre", unique=True, null=False, blank=False,
    )

    name = models.CharField(
        verbose_name="Nom du produit", null=False, blank=False, max_length=100,
    )

    common_name = models.CharField(
        verbose_name="Nom générique", blank=True, max_length=100,
    )

    quantity = models.CharField(verbose_name="Quantité", blank=True, max_length=50)

    ingredients_text = models.TextField(verbose_name="Ingrédients", blank=True)
    nutriscore_grade = models.CharField(
        verbose_name="Nutriscore", null=False, blank=False, max_length=1
    )

    url = models.CharField(
        verbose_name="Url du produit", null=False, blank=False, max_length=250
    )
    url_image = models.CharField(
        verbose_name="Url image du produit", blank=True, max_length=250
    )
    url_image_small = models.CharField(
        verbose_name="Url petite image du produit", blank=True, max_length=250,
    )

    categories = models.ManyToManyField(Category)
    stores = models.ManyToManyField(Store)
    brands = models.ManyToManyField(Brand)

    def __str__(self):
        return f"{self.code} - {self.name}"
