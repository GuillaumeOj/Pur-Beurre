from django.test import TestCase
from django.db.models import QuerySet

from product.models import Product


class ProductMangerTests(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

    def get_nutella(self):
        return Product.objects.filter(name="Nutella").first()

    def get_nut(self):
        return Product.objects.filter(name__icontains="nut").first()

    def test_get_product(self):
        product_code = self.get_nutella().code

        product = Product.objects.get_product(product_code)

        self.assertIsInstance(product, Product)
        self.assertEqual(product.code, product_code)

    def test_find_product_with_exact_name(self):
        nutella = self.get_nutella()

        product = Product.objects.find_product("Nutella")

        self.assertIsInstance(product, Product)
        self.assertEqual(product, nutella)

    def test_find_product_with_part_of_name(self):
        nutella = self.get_nut()

        product = Product.objects.find_product("nut")

        self.assertIsInstance(product, Product)
        self.assertEqual(product, nutella)

    def test_find_products(self):
        products = Product.objects.find_products("nut")

        self.assertIsInstance(products, QuerySet)
        self.assertLessEqual(len(products), 10)
        for product in products:
            self.assertIn("nut", product.name.lower())

    def test_find_substitutes(self):
        nutella = self.get_nutella()

        substitutes = Product.objects.find_substitutes(nutella.code)

        self.assertIsInstance(substitutes, QuerySet)
        self.assertLessEqual(len(substitutes), 30)
        self.assertTrue(substitutes.ordered)
        for substitute in substitutes:
            self.assertLess(substitute.nutriscore_grade, nutella.nutriscore_grade)
            self.assertNotEqual(substitute, nutella)
