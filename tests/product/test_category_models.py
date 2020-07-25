from django.test import TestCase

from product.models import Category


class CategoryModelsTests(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

    def get_category(self):
        return Category.objects.all().first()

    def test_category_printing_name(self):
        category = self.get_category()

        self.assertIsInstance(category, Category)
        self.assertEqual(category.__str__(), category.name)
