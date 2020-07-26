from django.test import TestCase

from product.forms import ProductSearchForm


class ProductSearchFormsTests(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

    def test_search_valid_form_with_two_characters(self):
        data = {"name": "nu"}
        form = ProductSearchForm(data=data)

        self.assertTrue(form.is_valid())

    def test_search_invalid_form_with_no_characters(self):
        data = {"name": ""}
        form = ProductSearchForm(data=data)

        self.assertFalse(form.is_valid())

    def test_search_invalid_form_with_one_character(self):
        data = {"name": "n"}
        form = ProductSearchForm(data=data)

        self.assertFalse(form.is_valid())

    def test_search_invalid_form_with_one_hundred_and_one_characters(self):
        data = {"name": 101 * "n"}
        form = ProductSearchForm(data=data)

        self.assertFalse(form.is_valid())
