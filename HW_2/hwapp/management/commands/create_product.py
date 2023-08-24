from django.core.management.base import BaseCommand
from hwapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        pruduct = Product(name='Sumsung A34',
                        description='A phone',
                        price=789.78,
                        count=34)
        pruduct.save()
        self.stdout.write(f'{pruduct}')
