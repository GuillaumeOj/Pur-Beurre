from django.core.management import BaseCommand, CommandError

from openfoodfacts.feed_db import FeedDb

class Command(BaseCommand):
    help = "Initialize the database with products from OpenFoodFacts"

    def handle(self, *args, **options):
        self.stdout.write("Downloading products from OpenFoodFacts")
        try:
            feeder = FeedDb()
            feeder.get_products()
