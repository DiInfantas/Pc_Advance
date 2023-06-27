from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    NombreCategoria =models.CharField(max_length=100)

    def __str__(self):
        return self.NombreCategoria

class Producto(models.Model):
    idProducto= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    precio=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

    