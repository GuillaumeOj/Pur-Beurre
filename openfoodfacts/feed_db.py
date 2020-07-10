from django.core.exceptions import ValidationError

from product.models import Product, Category, Store, Brand


class FeedDb:
    """
    Get products from OpenFoodFacts by using the class Api
    Normalize the data
    Insert the product and associated categories, brands, stores in the database
    """

    def feed_db(self, raw_products):

        # Insert each product in the application's database
        for raw_product in raw_products:
            normalized_product = self._normalize_product(raw_product)

            try:
                product = Product(
                    code=normalized_product["code"],
                    name=normalized_product["name"],
                    url=normalized_product["url"],
                    nutriscore_grade=normalized_product["nutriscore_grade"],
                    generic_name=normalized_product["generic_name"],
                    quantity=normalized_product["quantity"],
                    ingredients_text=normalized_product["ingredients_text"],
                    image_url=normalized_product["image_url"],
                    image_small_url=normalized_product["image_small_url"],
                )
                product.full_clean()
                product.save()
            except ValidationError:
                break

            # Insert associated categories, stores and brands
            for category in normalized_product["categories"]:
                obj, created = Category.objects.get_or_create(name=category)
                try:
                    obj.full_clean()
                    product.categories.add(obj)
                except ValidationError:
                    break
            for store in normalized_product["stores"]:
                obj, created = Store.objects.get_or_create(name=store)
                try:
                    obj.full_clean()
                    product.stores.add(obj)
                except ValidationError:
                    break
            for brand in normalized_product["brands"]:
                obj, created = Brand.objects.get_or_create(name=brand)
                try:
                    obj.full_clean()
                    product.brands.add(obj)
                except ValidationError:
                    break

    def _normalize_product(self, raw_product):
        """
        Normalize the product data
        """

        normalized = dict()

        normalized["code"] = raw_product.get("code")
        normalized["name"] = raw_product.get("product_name", "").title()
        normalized["url"] = raw_product.get("url", "").lower()
        normalized["nutriscore_grade"] = raw_product.get("nutriscore_grade", "").upper()

        normalized["generic_name"] = raw_product.get("generic_name_fr", "").capitalize()
        normalized["quantity"] = raw_product.get("quantity", "")
        normalized["ingredients_text"] = raw_product.get("ingredients_text", "")

        normalized["image_url"] = raw_product.get("image_url", "")
        normalized["image_small_url"] = raw_product.get("image_small_url", "")

        normalized["categories"] = raw_product.get("categories", "").split(",")
        normalized["stores"] = raw_product.get("stores", "").split(",")
        normalized["brands"] = raw_product.get("brands", "").split(",")

        return normalized
