from product.models import Category
from tests.custom import CustomTestCase


class CategoryModelsTests(CustomTestCase):
    def setUp(self):
        self.category = Category.objects.all().first()

    def test_category_printing_name(self):
        category = self.category

        self.assertIsInstance(category, Category)
        self.assertEqual(category.__str__(), category.name)
