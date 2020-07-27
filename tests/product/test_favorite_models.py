from product.models import Favorite, Product
from tests.custom import CustomTestCase


class FavoriteModelsTests(CustomTestCase):
    def setUp(self):
        self.product = Product.objects.filter(name="Nutella").first()
        self.substitute = Product.objects.filter(
            name="Pâte À Tartiner Chocolat Noisette"
        ).first()

    def test_category_printing_name(self):
        favorite = Favorite.objects.create(
            product=self.product, substitute=self.substitute
        )

        self.assertIsInstance(favorite, Favorite)
        self.assertEqual(
            favorite.__str__(),
            f"Produit : {favorite.product} / Substitut : {favorite.substitute}",
        )
