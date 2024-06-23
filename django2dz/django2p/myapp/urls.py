from django.urls import path
from .views import create_client, client_list, create_product, product_list, create_order, order_list

urlpatterns = [
    path('clients/new/', create_client, name='create_client'),
    path('clients/', client_list, name='client_list'),
    path('products/new/', create_product, name='create_product'),
    path('products/', product_list, name='product_list'),
    path('orders/new/', create_order, name='create_order'),
    path('orders/', order_list, name='order_list'),
]