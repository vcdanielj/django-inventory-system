from django.apps import apps
from django.db.models import Sum

def get_quantity(product_barcode):

    Product = apps.get_model('inventory', 'Product')
    OrderDetail = apps.get_model('store', 'OrderDetail')
    try:
        product = Product.objects.get(barcode=product_barcode)

        order_details = OrderDetail.objects.filter(product=product)
        in_quantity = order_details.filter(order__type='I').aggregate(Sum('quantity'))['quantity__sum'] or 0
        out_quantity = order_details.filter(order__type='O').aggregate(Sum('quantity'))['quantity__sum'] or 0

        return in_quantity - out_quantity

    except Product.DoesNotExist:
        return 0

# try:
#     product = Product.objects.get(barcode=1)
#     quantity = 0
#     order_details = OrderDetail.objects.filter(product=product)
#     for order_detail in order_details:
#         order_type = order_detail.order.type
#         if order_type == 'I':
#             quantity += order_detail.quantity
#         else:
#             quantity -= order_detail.quantity
#     print(quantity) 
# except Product.DoesNotExist:
#     print(0)