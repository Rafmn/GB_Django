from django.contrib import admin
from .models import Customer, Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    ordering = ['name']
    list_filter = ['date_add', 'price']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    ordering = ['name']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
