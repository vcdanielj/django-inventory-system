from django.db import models

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
    barcode = models.CharField(max_length=20, verbose_name="Código de Barra")
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, verbose_name="Marca")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Categoria")
    quantity = 0
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name