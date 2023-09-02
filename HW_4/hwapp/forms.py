import datetime
from django import forms
from . import models


class CustomerForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(label='Номер телефоана', max_length=15)
    address = forms.CharField(label='Адрес', max_length=100)
    date_reg = forms.DateTimeField(label='Дата регистрации', initial=datetime.date.today)

class ProductForm(forms.Form):
    name = forms.CharField(label='Наименование', max_length=100)
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    price = forms.DecimalField(label='Цена', max_digits=8, decimal_places=2)
    count = forms.IntegerField(label='Количество')
    date_add = forms.DateTimeField(label='Дата добавления', initial=datetime.date.today)
    image = forms.ImageField()

class OrderForm(forms.Form):
    customer = forms.ModelChoiceField(label='Посетилели', queryset=models.Customer.objects.all())
    product = forms.ModelChoiceField(label='Товары', queryset=models.Product.objects.all())
    total_price = forms.DecimalField(label='Полная стоимость', decimal_places=2)
    date_ordered = forms.DateTimeField(label='Дата заказа', initial=datetime.date.today)
