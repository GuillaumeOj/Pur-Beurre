from django.db import models

from product.models import Product


class Favorite(models.Model):
    """A favorite saved by a user."""

    # Required fields
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_product"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_substitute"
    )

    def __str__(self):
        return f"Produit : {self.product} / Substitut : {self.substitute}"
