from django.contrib.auth.models import AbstractUser
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    foto = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    foto = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

class Suscriptor(models.Model):
    nombreCompleto = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_suscripcion = models.DateTimeField(auto_now_add=True)

#Finalmente no utilice esta calase, pero la dejo por si en un futuro proyecto la necesito
class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)  # Campo opcional para avatar   
    
class Articulos(models.Model):
    TIPO_CHOICES = [
        ('producto', 'Producto'),
        ('repuesto', 'Repuesto'),
    ]
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    foto = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

