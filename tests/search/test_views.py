from json import loads
from unittest.mock import patch

from django.shortcuts import reverse
from django.test import override_settings

from product.models import Product
from tests.custom import CustomTestCase


class MockProductManager:
    def __init__(self, products, substitutes):
        self.products = products
        self.substitutes = substitutes

    def get_product_by_code(self, *args, **kwargs):
        return self.products

    def get_product_by_name(self, *args, **kwargs):
        return self.products

    def get_products_by_name(self, *args, **kwargs):
        return self.products

    def find_substitutes(self, *args, **kwargs):
        return self.substitutes


class MockProduct:
    def __init__(self, products, substitutes=""):
        self.objects = MockProductManager(products, substitutes)


@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class SearchViewsAutoCompletionTests(CustomTestCase):
    def setUp(self):
        self.products = Product.objects.filter(name__icontains="nut")[:2]

    def test_auto_completion_return_json(self):
        url = reverse("search:auto_completion")
        mock_product = MockProduct(self.products).objects.get_products_by_name
        with patch("product.models.Product", mock_product):
            response = self.client.post(url, data={"name": "nut"})

            self.assertEqual(response.status_code, 200)
            self.assertTrue(loads(response.content).get("products_names"))

    def test_auto_completion_return_empty_list_if_there_is_no_matching_product(self):
        url = reverse("search:auto_completion")
        mock_product = MockProduct(self.products).objects.get_products_by_name
        with patch("product.models.Product", mock_product):
            response = self.client.post(url, data={"name": "qwerty"})

            self.assertEqual(response.status_code, 200)
            self.assertIn("products_names", loads(response.content))
            self.assertEqual(loads(response.content).get("products_names"), [])

    def test_auto_completion_return_no_json_if_the_form_is_invalid(self):
        url = reverse("search:auto_completion")
        mock_product = MockProduct(self.products).objects.get_products_by_name
        with patch("product.models.Product", mock_product):
            response = self.client.post(url, data={"name": ""})

            self.assertEqual(response.status_code, 400)

    def test_auto_completion_redirect_if_accessing_with_get(self):
        url = reverse("search:auto_completion")
        mock_product = MockProduct(self.products).objects.get_products_by_name
        with patch("product.models.Product", mock_product):
            response = self.client.get(url)

            self.assertEqual(response.status_code, 302)


@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class SearchViewsGetProductTests(CustomTestCase):
    def setUp(self):
        self.nutella = Product.objects.filter(name="Nutella").first()

    def test_get_product_redirect_to_get_substitutes_if_found_a_product(self):
        url = reverse("search:get_product")
        mock_product = MockProduct(self.nutella).objects.get_product_by_name
        with patch("product.models.Product", mock_product):
            response = self.client.post(url, data={"name": "Nutella"})

            self.assertEqual(response.status_code, 302)

    def test_get_product_render_page_if_no_product_was_found(self):
        url = reverse("search:get_product")
        mock_product = MockProduct(self.nutella).objects.get_product_by_name
        with patch("product.models.Product", mock_product):
            response = self.client.post(url, data={"name": "qwerty"})

            self.assertEqual(response.status_code, 200)

    def test_get_product_redirect_if_accessing_with_get(self):
        url = reverse("search:get_product")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)


@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class SearchViewsGetSubstitutesTests(CustomTestCase):
    def setUp(self):
        self.nutella = Product.objects.filter(name="Nutella").first()
        self.substitutes = Product.objects.all().order_by("name")[:30]

    def test_get_substitutes_is_loading_with_correct_product(self):
        url = reverse("search:get_substitutes", args=[self.nutella.code])
        mock_product = MockProduct(self.nutella, self.substitutes).objects
        with patch("product.models.Product.objects", mock_product):
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)

    def test_get_substitutes_is_loading_with_wrong_product_code(self):
        url = reverse("search:get_substitutes", args=["wrong_code"])
        mock_product = MockProduct(self.nutella, self.substitutes).objects
        with patch("product.models.Product.objects", mock_product):
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)

    def test_get_substitutes_is_loading_with_page_number_is_not_integer(self):
        url = reverse(
            "search:get_substitutes", args=[self.nutella.code, "wrong_page_number"]
        )
        mock_product = MockProduct(self.nutella, self.substitutes).objects
        with patch("product.models.Product.objects", mock_product):
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)

    def test_get_substitutes_is_loading_with_no_page_number(self):
        url = reverse("search:get_substitutes", args=[self.nutella.code])
        mock_product = MockProduct(self.nutella, self.substitutes).objects
        with patch("product.models.Product.objects", mock_product):
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)

    def test_get_substitutes_is_loading_with_wrong_page_number(self):
        url = reverse("search:get_substitutes", args=[self.nutella.code, 150])
        mock_product = MockProduct(self.nutella, self.substitutes).objects
        with patch("product.models.Product.objects", mock_product):
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
