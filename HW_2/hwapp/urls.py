from .views import customer_products
from django.urls import path

urlpatterns = [
    # path('', my_view, name='index'),
    path('customer/<int:customer_id>', customer_products, name='customer'),
]
