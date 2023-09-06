from django.core.management.base import BaseCommand
from hwapp.models import Customer


class Command(BaseCommand):
    help = "Create customer."

    def handle(self, *args, **kwargs):
        user = Customer(name='Ivan',
                        email='Inam@example.com',
                        phone='34779123',
                        address='Bugulma, Baumana 435-5')
        user.save()
        self.stdout.write(f'{user}')
