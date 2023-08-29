from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Order
from datetime import timedelta, datetime

def customer_products(request, customer_id):
    customer = Customer.objects.filter(pk=customer_id).first()
    orders = Order.objects.filter(customer=customer)
    orders_products = {}
    for order in orders:
        products = Order.objects.get(id=order.id).product.all()
        orders_products[order] = products

    return render(request, "hwapp/customer_product.html", {'customer': customer, 'products': products})
