from product.forms import ProductSearchForm
from tests.custom import CustomTestCase


class ProductSearchFormsTests(CustomTestCase):
    def test_search_form_with_two_characters_is_valid(self):
        data = {"name": "nu"}
        form = ProductSearchForm(data=data)

        self.assertTrue(form.is_valid())

    def test_search_form_with_no_characters_is_invalid(self):
        data = {"name": ""}
        form = ProductSearchForm(data=data)

        self.assertFalse(form.is_valid())

    def test_search_form_with_one_character_is_invalid(self):
        data = {"name": "n"}
        form = ProductSearchForm(data=data)

        self.assertFalse(form.is_valid())

    def test_search_form_with_more_than_hundred_characters_is_invalid(self):
        data = {"name": 101 * "n"}
        form = ProductSearchForm(data=data)

        self.assertFalse(form.is_valid())
