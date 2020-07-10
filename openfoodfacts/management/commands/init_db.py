from django.core.management import BaseCommand

from openfoodfacts.api import Api
from openfoodfacts.feed_db import FeedDb


class Command(BaseCommand):
    help = "Initialize the database with products from OpenFoodFacts"

    def handle(self, *args, **options):
        self.stdout.write("Downloading products from OpenFoodFacts")
        api = Api()
        raw_products = api.get_products()

        self.stdout.write(self.style.SUCCESS("Done."))

        self.stdout.write("Inserting products in the database")
        feeder = FeedDb()
        feeder.feed_db(raw_products)

        self.stdout.write(self.style.SUCCESS("Done."))
