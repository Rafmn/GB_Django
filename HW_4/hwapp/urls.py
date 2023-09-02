from django.urls import path
from .views import customer_form, order_form, product_form


urlpatterns = [
    path('customer_add/', customer_form, name='customer_form'),
    path('product_add/', product_form, name='product_form'),
    path('order_add/<int:customer_id> <int:product_id>', order_form, name='order_form'),
    # path('upload/', upload_image, name='upload_image'),
]
