from django.contrib import admin
from .models import Producto, Repuesto, Suscriptor, Datos

# Registro los modelos en el panel de administración
admin.site.register(Producto)
admin.site.register(Repuesto)
admin.site.register(Suscriptor)
admin.site.register(Datos)  