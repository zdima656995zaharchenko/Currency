import random
from django.core.management.base import BaseCommand
from currency.models import Rate, Source
from currency.choices import CurrencyChoices


class Command(BaseCommand):
    help = "Generates dummy rates data"

    def handle(self, *args, **options):

        source, _ = Source.objects.get_or_create(
            code_name='dummy',
            defaults={
                'name': 'Dummy source'
            }
        )

        for _ in range(400):
            Rate.objects.create(
                buy=random.randint(30,40),
                sell=random.randint(30,40),
                currency=random.choice(CurrencyChoices.choices)[0],
                source=source

            )

        self.stdout.write(
                self.style.SUCCESS('Successfully generated dummy data!')
         )