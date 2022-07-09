from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    comentarios = models.TextField()
    fecha_alta = models.DateField(auto_now_add=True)
    
class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='articulos')
    fecha_alta = models.DateField(auto_now_add=True)
    