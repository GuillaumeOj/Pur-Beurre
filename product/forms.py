from django import forms

from product.models import Product


class ProductSearchForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Chercher un aliment"}),
    )

    class Meta:
        model = Product
        fields = ["name"]
