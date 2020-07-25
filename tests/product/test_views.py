from django.test import TestCase, override_settings
from django.shortcuts import reverse

from product.models import Product
from users.models import User


@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class ProductViewsTests(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

    def setUp(self):
        self.user = User.objects.all().first()

    def get_nutella(self):
        return Product.objects.filter(name__icontains="nut").first()

    def test_sheet_is_loading(self):
        nutella = self.get_nutella()

        url = reverse("product:sheet", args=[nutella.code])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_favorites_is_loading(self):
        self.client.force_login(self.user)
        url = reverse("product:favorites")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
