from django.test import TestCase

from product.models import Favorite, Product


class FavoriteModelsTests(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

    def create_favorite(self):
        product = Product.objects.filter(name="Nutella").first()
        substitute = Product.objects.filter(
            name="Pâte À Tartiner Chocolat Noisette"
        ).first()

        return Favorite.objects.create(product=product, substitute=substitute)

    def test_category_printing_name(self):
        favorite = self.create_favorite()

        self.assertIsInstance(favorite, Favorite)
        self.assertEqual(
            favorite.__str__(),
            f"Produit : {favorite.product} / Substitut : {favorite.substitute}",
        )
