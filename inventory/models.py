from django.db import models
from django.forms import ValidationError
from .utils import get_quantity
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
    barcode = models.CharField(max_length=20, verbose_name="Número de Inventario", unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, verbose_name="Marca")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Categoria")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def quantity(self):
        return get_quantity(self.barcode)
    
    def clean(self):
        # Comprobar si existe un producto con el mismo barcode
        if Product.objects.filter(barcode=self.barcode).exists():
            raise ValidationError('Ya existe un producto con el número de inventario proporcionado.')