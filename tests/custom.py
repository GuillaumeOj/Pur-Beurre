from django.test import TestCase


class CustomTestCase(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

