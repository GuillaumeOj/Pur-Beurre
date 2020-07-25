from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Category(models.Model):
    """Category for a product."""

    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(1), MaxLengthValidator],
    )

    def __str__(self):
        return self.name

