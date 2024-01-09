from django.db import models
from inventory.models import Product

class Buyer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    addres = models.CharField(max_length=500, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    addres = models.CharField(max_length=500, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    INPUT = 'I'
    OUTPUT = 'O'
    TYPE_CHOICES = [
        (INPUT, 'In'),
        (OUTPUT, 'Out')
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name="Tipo")
    date = models.DateField(verbose_name="Fecha")
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Proveedor")
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Personal")
    observation = models.CharField(max_length=500, verbose_name="Observación")
    user = models.IntegerField(null=True, blank=True, verbose_name="Usuario")

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name="Orden")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="Producto")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad")
