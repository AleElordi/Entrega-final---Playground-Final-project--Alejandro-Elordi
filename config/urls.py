"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppCoder.views import datos, productos, repuestos, suscriptores, inicio 

urlpatterns = [
    path('', inicio, name='inicio'),
    path('datos/', datos, name='datos'),
    path('productos/', productos, name='productos'),
    path('repuestos/', repuestos, name='repuestos'),
    path('suscriptores/', suscriptores, name='suscriptores'),
]