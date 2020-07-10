from django.db import models
from django.core.exceptions import ValidationError


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


class ProductManager(models.Manager):
    def create_product(self, raw_product):
        if self._valid_raw_product(raw_product):
            product = self.create(
                code=raw_product["code"],
                name=raw_product["name"],
                url=raw_product["url"],
                nutriscore_grade=raw_product["nutriscore_grade"],
                generic_name=raw_product["generic_name"],
                quantity=raw_product["quantity"],
                ingredients_text=raw_product["ingredients_text"],
                image_url=raw_product["image_url"],
                image_small_url=raw_product["image_small_url"],
            )
            return product

    def _valid_raw_product(self, raw_product):
        """
        Validate the raw product's data
        """
        # Required fields
        if not raw_product.get("code"):
            raise ValidationError("Missing product's code")
        if len(raw_product.get("code")) != 13:
            raise ValidationError("Product's code is not at EAN-13 format")

        if not raw_product.get("name"):
            raise ValidationError("Missing product's name")
        if len(raw_product.get("name")) > 100:
            raise ValidationError("Product's name too long")

        if not raw_product.get("nutriscore_grade"):
            raise ValidationError("Missing product's nutriscore grade")
        if len(raw_product.get("nutriscore_grade")) > 1:
            raise ValidationError("Product's nutriscore grade too long")

        if not raw_product.get("url"):
            raise ValidationError("Missing product's url")
        if len(raw_product.get("url")) > 250:
            raise ValidationError("Product's url too long")

        # Optionnal fields
        if raw_product.get("generic_name") and len(raw_product.get("generic_name")) > 100:
            raise ValidationError("Product's generic name too long")

        if raw_product.get("quantity") and len(raw_product.get("quantity")) > 100:
            raise ValidationError("Product's quantity too long")

        return True


class Product(models.Model):
    """
    Product from openfoodfact
    """

    code = models.CharField(max_length=13, unique=True)

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

    objects = ProductManager()

    def __str__(self):
        return f"{self.code} - {self.name}"
