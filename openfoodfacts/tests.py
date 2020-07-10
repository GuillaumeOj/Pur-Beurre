from django.test import TestCase

from product.models import Product
from openfoodfacts.feed_db import FeedDb


# Create your tests here.
class FeedDbModelsTests(TestCase):
    def test_insert_product_with_all_required_fields(self):
        data = [
            {
                "nutriscore_grade": "d",
                "code": "7622210449283",
                "url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet-lu",
                "product_name": "Prince goût chocolat au blé complet",
            }
        ]
        feeder = FeedDb()
        feeder.feed_db(data)
        product = Product.objects.filter(code="7622210449283")

        self.assertTrue(product)

    def test_insert_product_without_a_nutriscore_grade(self):
        data = [
            {
                "code": "7622210449283",
                "url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet-lu",
                "product_name": "Prince goût chocolat au blé complet",
            }
        ]
        feeder = FeedDb()
        feeder.feed_db(data)
        product = Product.objects.filter(code="7622210449283")

        self.assertFalse(product)

    def test_insert_product_without_a_code(self):
        data = [
            {
                "nutriscore_grade": "d",
                "url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet-lu",
                "product_name": "Prince goût chocolat au blé complet",
            }
        ]
        feeder = FeedDb()
        feeder.feed_db(data)
        product = Product.objects.filter(nutriscore_grade="d")

        self.assertFalse(product)

    def test_insert_product_without_an_url(self):
        data = [
            {
                "nutriscore_grade": "d",
                "code": "7622210449283",
                "product_name": "Prince goût chocolat au blé complet",
            }
        ]
        feeder = FeedDb()
        feeder.feed_db(data)
        product = Product.objects.filter(code="7622210449283")

        self.assertFalse(product)

    def test_insert_product_code_too_long(self):
        data = [
            {
                "nutriscore_grade": "de",
                "code": "7622210449283",
                "url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet-lu",
                "product_name": "Prince goût chocolat au blé complet",
            }
        ]
        feeder = FeedDb()
        feeder.feed_db(data)
        product = Product.objects.filter(code="7622210449283")

        self.assertFalse(product)
