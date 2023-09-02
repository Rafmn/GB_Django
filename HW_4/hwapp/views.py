from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .forms import ProductForm, CustomerForm, OrderForm
import logging
from . import models

logger = logging.getLogger(__name__)
 

def customer_form(request):
    message = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = models.Customer(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )
            customer.save()
            message = 'Посетитель успешно сохранен'
    else:
        form = CustomerForm()
    return render(request, 'hwapp/main_form.html',
                  {'form': form, 'message': message, 'title': 'Сохранение посетителя'})


def product_form(request):
    message = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image=form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = models.Product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                count=form.cleaned_data['count'],
                date_add=form.cleaned_data['date_add'],
                image = image
            )
            product.save()
            message = 'Товар успешно сохранен'
    else:
        form = ProductForm()
    return render(request, 'hwapp/main_form.html',
                  {'form': form, 'message': message, 'title': 'Сохранение товара'})

# def upload_image(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#     else:
#         form = ProductForm()
#     return render(request, 'hwapp/upload_image.html', {'form': form})


def order_form(request, customer_id, product_id):
    message = ''
    customer = models.Customer.objects.filter(pk=customer_id).first()
    product = models.Product.objects.filter(pk=product_id).first()
    orders = models.Order.objects.filter(customer=customer)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = models.Order(
                customer=customer,
                product=product,
                total_price=form.cleaned_data['total_price'],
                date_ordered=form.cleaned_data['date_ordered'],
            )
            order.save()
            message = 'Заказ оформлен'
    else:
        form = OrderForm()
    return render(request, 'hwapp/order_form.html',
                  {'form': form, 'customer': customer, 'product': product, 'message': message, 'orders': orders, 'title': 'Добавление заказа'})
