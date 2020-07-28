from django.db.models import QuerySet

from product.models import Product
from tests.custom import CustomTestCase


class ProductManagerTests(CustomTestCase):
    def setUp(self):
        self.nutella = Product.objects.filter(name="Nutella").first()
        self.nut = Product.objects.filter(name__icontains="nut").first()

    def test_get_product_by_code(self):
        product = Product.objects.get_product_by_code(self.nutella.code)

        self.assertIsInstance(product, Product)
        self.assertEqual(product.code, self.nutella.code)

    def test_get_product_by_code_with_wrong_code(self):
        product = Product.objects.get_product_by_code("qwerty")

        self.assertFalse(product)

    def test_get_product_by_code_with_no_code(self):
        product = Product.objects.get_product_by_code("")

        self.assertFalse(product)

    def test_get_product_by_name_with_exact_name(self):
        product = Product.objects.get_product_by_name("Nutella")

        self.assertIsInstance(product, Product)
        self.assertEqual(product, self.nutella)

    def test_get_product_by_name_with_part_of_name(self):
        product = Product.objects.get_product_by_name("nut")

        self.assertEqual(product, self.nut)

    def test_get_product_by_name_with_wrong_name(self):
        product = Product.objects.get_product_by_name("qwerty")

        self.assertFalse(product)

    def test_get_product_by_name_with_no_name(self):
        product = Product.objects.get_product_by_name("")

        self.assertFalse(product)

    def test_get_products_by_name(self):
        products = Product.objects.get_products_by_name("nut")

        self.assertIsInstance(products, QuerySet)
        self.assertLessEqual(len(products), 10)
        for product in products:
            self.assertIn("nut", product.name.lower())

    def test_get_products_by_name_with_wrong_name(self):
        products = Product.objects.get_products_by_name("qwerty")

        self.assertFalse(products)

    def test_get_products_by_name_with_no_name(self):
        products = Product.objects.get_products_by_name("")

        self.assertFalse(products)

    def test_find_substitutes(self):
        substitutes = Product.objects.find_substitutes(self.nutella.code)

        self.assertIsInstance(substitutes, QuerySet)
        self.assertLessEqual(len(substitutes), 30)
        self.assertTrue(substitutes.ordered)
        for substitute in substitutes:
            self.assertLess(substitute.nutriscore_grade, self.nutella.nutriscore_grade)
            self.assertNotEqual(substitute, self.nutella)

    def test_find_substitutes_with_wrong_code(self):
        substitutes = Product.objects.find_substitutes("qwerty")

        self.assertFalse(substitutes)

    def test_find_substitutes_with_no_code(self):
        substitutes = Product.objects.find_substitutes("")

        self.assertFalse(substitutes)
