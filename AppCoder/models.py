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

class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

