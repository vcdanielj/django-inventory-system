from django.db import models
from .models import Product, OrderDetail


try:
    product = Product.objects.get(barcode=1)
    quantity = 0
    order_details = OrderDetail.objects.filter(product=product)
    for order_detail in order_details:
        order_type = order_detail.order.type
        if order_type == 'I':
            quantity += order_detail.quantity
        else:
            quantity -= order_detail.quantity
    print(quantity) 
except Product.DoesNotExist:
    print(0)