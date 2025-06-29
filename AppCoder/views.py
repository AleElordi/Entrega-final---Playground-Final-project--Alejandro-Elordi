from django.shortcuts import render

def inicio(request):
    return render(request, "AppCoder/index.html")

def datos(request):
    return render(request, "AppCoder/datos.html")

def productos(request):
    return render(request, "AppCoder/productos.html")

def repuestos(request):
    return render(request, "AppCoder/repuestos.html")

def suscriptores(request):
    return render(request, "AppCoder/suscriptores.html")
