import pandas as pd

from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):
    help = "Import products from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **options):
        csv_file = options["csv_file"]

        df = pd.read_csv(csv_file)

        for _, row in df.iterrows():

            Product.objects.update_or_create(
                external_id=row["External ID"],
                defaults={
                    "name": row["Name"],
                    "product_type": "Other",
                    "internal_reference": row["Internal Reference"],
                    "description": row["Sales Description"],
                    "weight": row["Weight (Kg)"],
                },
            )

        self.stdout.write(
            self.style.SUCCESS("Products imported successfully!")
        )