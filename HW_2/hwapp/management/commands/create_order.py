from random import choice, randint
from django.core.management.base import BaseCommand
from hwapp.models import Customer, Order, Product


class Command(BaseCommand):
    help = "Create orders."

    def handle(self, *args, **kwargs):
        products=Product.objects.all()
        for customer in Customer.objects.all():
            order = Order.objects.create(customer=customer)
            price_prs = 0
            for _ in range(randint(1, 7)):
                product = choice(products)
                order.product.add(product)
                price_prs += product.price
            order.total_price = price_prs
            order.save()
        self.stdout.write('orders created')
