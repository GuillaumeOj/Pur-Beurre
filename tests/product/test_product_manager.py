from django.db.models import QuerySet

from product.models import Product
from tests.custom import CustomTestCase


class ProductMangerTests(CustomTestCase):
    def setUp(self):
        self.nutella = Product.objects.filter(name="Nutella").first()
        self.nut = Product.objects.filter(name__icontains="nut").first()

    def test_get_product(self):
        product = Product.objects.get_product(self.nutella.code)

        self.assertIsInstance(product, Product)
        self.assertEqual(product.code, self.nutella.code)

    def test_get_product_with_wrong_code(self):
        product = Product.objects.get_product("qwerty")

        self.assertFalse(product)

    def test_find_product_with_exact_name(self):
        product = Product.objects.find_product("Nutella")

        self.assertIsInstance(product, Product)
        self.assertEqual(product, self.nutella)

    def test_find_product_with_part_of_name(self):
        product = Product.objects.find_product("nut")

        self.assertIsInstance(product, Product)
        self.assertEqual(product, self.nut)

    def test_find_product_with_wrong_name(self):
        product = Product.objects.find_product("qwerty")

        self.assertNotIsInstance(product, Product)
        self.assertFalse(product)

    def test_find_products(self):
        products = Product.objects.find_products("nut")

        self.assertIsInstance(products, QuerySet)
        self.assertLessEqual(len(products), 10)
        for product in products:
            self.assertIn("nut", product.name.lower())

    def test_find_substitutes(self):
        substitutes = Product.objects.find_substitutes(self.nutella.code)

        self.assertIsInstance(substitutes, QuerySet)
        self.assertLessEqual(len(substitutes), 30)
        self.assertTrue(substitutes.ordered)
        for substitute in substitutes:
            self.assertLess(substitute.nutriscore_grade, self.nutella.nutriscore_grade)
            self.assertNotEqual(substitute, self.nutella)
