from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from product.models import Product


class Search(forms.ModelForm):
    class Meta:
        name = forms.CharField(
            min_length=2,
            max_length=100,
            validators=[MinLengthValidator, MaxLengthValidator],
        )
        model = Product
        fields = ["name"]
