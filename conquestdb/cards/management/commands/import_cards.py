import pandas as pd
from django.core.management.base import BaseCommand
from cards.models import Card
from card_utils import convert_name_to_hyperlink

class Command(BaseCommand):
    help = "Import or update cards from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_path")

    def handle(self, *args, **opts):
        df = pd.read_csv(opts["csv_path"])
        # Turn NaN into None so nullable fields work
        df = df.astype(object).where(df.notna(), None)
        created = updated = 0
        for row in df.to_dict(orient="records"):
            print(row)
            _, was_created = Card.objects.update_or_create(
                code=convert_name_to_hyperlink(row["name"]).replace("/cards/", ""),
                defaults={
                    "name": row["name"],
                    "faction": row["faction"] if row["card type"] != "Planet" else "",
                    "loyalty": row["loyalty"] if row["card type"] != "Planet" else "",
                    "text": row["text"],
                    "card_type": row["card type"],
                    "cost": row["cost"],
                    "command": row["command"],
                    "attack": row["attack"],
                    "health": row["health"],
                    "shields": row["shields"],
                    "cycle": row["cycle"],
                    "war_pack": row["war pack"],
                    "keywords": row["keywords"],
                    "useful_quantities": row["useful_quantities"],
                    "sector": row["sector"] if row["card type"] == "Planet" else "",
                    "green": row["green"] if row["card type"] == "Planet" else False,
                    "blue": row["blue"] if row["card type"] == "Planet" else False,
                    "red": row["red"] if row["card type"] == "Planet" else False,
                    "resources": row["resources"] if row["card type"] == "Planet" else 0,
                    "cards": row["cards"] if row["card type"] == "Planet" else 0,
                },
            )
            created += was_created
            updated += not was_created

        self.stdout.write(f"{created} created, {updated} updated")