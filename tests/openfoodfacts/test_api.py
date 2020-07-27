from unittest.mock import patch

from django.test import TestCase

from openfoodfacts.api import Api


def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            return True

    data = {
        "products": [
            {
                "nutriscore_grade": "d",
                "code": "7622210449283",
                "url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet",
                "product_name": "Prince goût chocolat au blé complet",
            }
        ]
    }
    return MockResponse(data, 200)


class FeedDbModelsTests(TestCase):
    @patch("openfoodfacts.api.requests.get", mock_requests_get)
    def test_api_return_products(self):
        products = Api().get_products()

        self.assertTrue(products)
