from django.urls import path
from .views import datos, productos, repuestos, suscriptores, inicio 

urlpatterns = [
    path('', inicio, name='inicio'),
    path('datos/', datos, name='datos'),
    path('productos/', productos, name='productos'),
    path('repuestos/', repuestos, name='repuestos'),
    path('suscriptores/', suscriptores, name='suscriptores'),
]