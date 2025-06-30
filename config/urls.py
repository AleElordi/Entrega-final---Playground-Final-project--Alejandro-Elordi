from django.urls import path
from django.contrib import admin
from AppCoder.views import datos, resBusqueda, suscriptores, inicio, buscador


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('datos/', datos, name='datos'),
    path('suscriptores/', suscriptores, name='suscriptores'),
    path('buscador/', buscador, name='buscador'),
    path('resBuscador/', resBusqueda, name='resBusqueda'),
]