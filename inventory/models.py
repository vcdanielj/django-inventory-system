from django.db import models
# import sqlite3
# from store.models import OrderDetail

def get_quantity(barcode):
    return 0
""" 
    try:
        product = Product.objects.get(barcode=barcode)
        quantity = 0
        order_details = OrderDetail.objects.filter(product=product)
        for order_detail in order_details:
            order_type = order_detail.order.type
            if order_type == 'I':
                quantity += order_detail.quantity
            else:
                quantity -= order_detail.quantity
        return quantity
    except Product.DoesNotExist:
        return 0
connection = sqlite3.connect('C:/Users/UJAP/Desktop/Softwares/Inventario Planta Física/db.sqlite3')

cursor = connection.cursor()

def get_quantity(barcode):
    row = cursor.execute('SELECT id FROM inventory_product WHERE barcode = ?', (str(barcode),)).fetchone()
    if row is not None:
        product_id = row[0]
    else:
        return 0
    quantity = 0
    cursor.execute('SELECT quantity, order_id FROM store_orderdetail WHERE product_id = ?', (product_id,))
    product_orders = cursor.fetchall()
    for product_order in product_orders:
        cursor.execute('SELECT type FROM store_order WHERE id = ?', (product_order[1],))
        order_type = cursor.fetchone()
        if order_type[0] == 'I':
            quantity += product_order[0]
        else:
            quantity -= product_order[0]

    print(f"{barcode}: {quantity}")
    return quantity
 """
class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    barcode = models.CharField(max_length=20, verbose_name="Número de Inventario")
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, verbose_name="Marca")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Categoria")
    quantity = get_quantity(barcode)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    