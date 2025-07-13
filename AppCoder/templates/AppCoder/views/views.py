from django.shortcuts import render
from ....models import  Suscriptor, Repuesto, Producto, Usuario, Articulos
from ....forms import datosSuscriptor, ProductoForm, RepuestoForm, RegistroUsuarioForm, ArticulosForm

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
    articulos = Articulos.objects.all()  # Si necesitas manejar artículos en general
    contexto = {
        "productos": productos,
        "repuestos": repuestos,
        "articulos": articulos,
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
    mensaje_producto = None
    mensaje_repuesto = None
    mensaje_articulo = None

    if request.method == 'POST':
        if 'producto_submit' in request.POST:
            producto_form = ProductoForm(request.POST)
            repuesto_form = RepuestoForm()
            if producto_form.is_valid():
                producto_form.save()
                mensaje_producto = "¡Producto agregado exitosamente!"
                producto_form = ProductoForm()
        elif 'repuesto_submit' in request.POST:
            repuesto_form = RepuestoForm(request.POST)
            producto_form = ProductoForm()
            if repuesto_form.is_valid():
                repuesto_form.save()
                mensaje_repuesto = "¡Repuesto agregado exitosamente!"
                repuesto_form = RepuestoForm()
        elif 'articulo_submit' in request.POST:
            articulo_form = ArticulosForm(request.POST)
            if articulo_form.is_valid():
                articulo_form.save()
                mensaje_articulo = "¡Artículo agregado exitosamente!"
                articulo_form = ArticulosForm()
    else:
        producto_form = ProductoForm()
        repuesto_form = RepuestoForm()
        articulo_form = ArticulosForm()

    return render(request, "AppCoder/articulos.html", {
        'producto_form': producto_form,
        'repuesto_form': repuesto_form,
        'articulo_form': articulo_form,
        'mensaje_articulo': mensaje_articulo,
        'mensaje_producto': mensaje_producto,
        'mensaje_repuesto': mensaje_repuesto,
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