from django.shortcuts import render
from .models import  Suscriptor, Repuesto, Producto
from .forms import datosSuscriptor

def inicio(request):
    return render(request, "AppCoder/index.html")

def datos(request):
    return render(request, "AppCoder/datos.html")

def suscriptores(request):
    mensaje_exito = None
    if request.method == 'POST':
        form = datosSuscriptor(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            # Verificar si ya existe un suscriptor con ese email
            if Suscriptor.objects.filter(email=informacion['email']).exists():
                # Si existe, mostrar un mensaje de error
                form.add_error('email', 'Este email ya está registrado.')
                return render(request, "AppCoder/suscriptores.html", {'form': form})
            suscriptor = Suscriptor(
                nombreCompleto=informacion['nombreCompleto'],
                email=informacion['email'],
                fecha_suscripcion=informacion['fecha_suscripcion']
            )
            suscriptor.save()
            # Genero un mensaje de éxito en caso de que la suscripción se realice correctamente
            mensaje_exito = "¡Te has suscripto exitosamente!"
            form = datosSuscriptor()  # Formulario vacío
    else:
        form = datosSuscriptor()

    return render(request, "AppCoder/suscriptores.html", {'form': form, 'mensaje_exito': mensaje_exito})

def buscador(request):
    productos = Producto.objects.all()
    repuestos = Repuesto.objects.all()
    contexto = {
        "productos": productos,
        "repuestos": repuestos,
    }
    return render(request, "AppCoder/buscadores/buscador.html", contexto)

def resBusqueda(request):
    marca = request.GET.get("marca", "")
    productos = Producto.objects.filter(marca__icontains=marca)
    repuestos = Repuesto.objects.filter(marca__icontains=marca)
    contexto = {
        "marca": marca,
        "productos": productos,
        "repuestos": repuestos,
    }
    return render(request, "AppCoder/buscadores/resBusqueda.html", contexto)