from django.test import TestCase, override_settings, Client
from django.shortcuts import reverse

from product.models import Product
from users.models import User


@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class ProductViewsTests(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

    def setUp(self):
        self.client = Client(HTTP_REFERER="http://www.qwant.fr")
        self.user = User.objects.all().first()

    def get_nutella(self):
        return Product.objects.filter(name__icontains="nut").first()

    def get_pate(self):
        return Product.objects.filter(name__icontains="Nocciolata").first()

    def test_sheet_is_loading(self):
        nutella = self.get_nutella()

        url = reverse("product:sheet", args=[nutella.code])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_save_favorite_is_redirecting(self):
        self.client.force_login(self.user)
        product = self.get_nutella()
        substitute = self.get_pate()

        url = reverse(
            "product:save",
            kwargs={"product_code": product.code, "substitute_code": substitute.code},
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_favorites_is_loading(self):
        self.client.force_login(self.user)
        url = reverse("product:favorites")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
