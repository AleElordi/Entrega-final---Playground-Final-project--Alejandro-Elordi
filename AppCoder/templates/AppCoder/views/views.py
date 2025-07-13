from django.shortcuts import render
from ....models import  Suscriptor, Repuesto, Producto, Usuario, Articulos
from ....forms import datosSuscriptor, RegistroUsuarioForm, ArticulosForm

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
    articulo = Articulos.objects.all() 
    contexto = {
        "articulos": articulo,
    }
    return render(request, "AppCoder/buscadores/buscador.html", contexto)

def resBusqueda(request):
    marca = request.GET.get("marca", "")
    productos = Producto.objects.filter(marca__icontains=marca)
    repuestos = Repuesto.objects.filter(marca__icontains=marca)
    articulo = Articulos.objects.filter(marca__icontains=marca)
    contexto = {
        "marca": marca,
        "productos": productos,
        "repuestos": repuestos,
        "articulos": articulo,  
    }
    return render(request, "AppCoder/buscadores/resBusqueda.html", contexto)

def articulos(request):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        articulo_form = ArticulosForm(request.POST)
        if articulo_form.is_valid():
            nombre = articulo_form.cleaned_data['nombre']
            marca = articulo_form.cleaned_data['marca']
            # Verifica si ya existe un artículo con ese nombre y marca
            if Articulos.objects.filter(nombre=nombre, marca=marca).exists():
                mensaje_error = "Ya existe un artículo con ese nombre y marca."
            else:
                articulo_form.save()
                mensaje_exito = "¡Artículo agregado exitosamente!"
                articulo_form = ArticulosForm()  # Formulario vacío tras guardar
    else:
        articulo_form = ArticulosForm()
    return render(request, "AppCoder/articulos.html", {
        'articulo_form': articulo_form,
        'mensaje_exito': mensaje_exito,
        'mensaje_error': mensaje_error,
    })

def registroUsuario(request):
    mensaje = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario = Usuario(
                username=informacion['username'],
                password=informacion['password'],
                email=informacion['email'],
                avatar=informacion.get('avatar', None)  # Manejo de avatar opcional
            )
            mensaje = "¡Usuario registrado exitosamente!"
            usuario.save()
            return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
    else:
        form = RegistroUsuarioForm() # Formulario vacío
    
    return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})