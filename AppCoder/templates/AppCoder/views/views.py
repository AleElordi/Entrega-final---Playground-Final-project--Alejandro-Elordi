from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ....models import  Suscriptor, Repuesto, Producto, Usuario, Articulos
from ....forms import datosSuscriptor, RegistroUsuarioForm, ArticulosForm, LoginForm
from django.contrib.auth.forms import PasswordChangeForm # Importa PasswordChangeForm para cambiar la contraseña


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
    articulos = Articulos.objects.all()
    contexto = {
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

@login_required # Asegura que solo usuarios autenticados puedan acceder a esta vista
def articulos(request):
    mensaje_exito = None
    mensaje_error = None
    articulos = Articulos.objects.all()  # <-- Agrega esta línea
    if request.method == "POST":
        articulo_form = ArticulosForm(request.POST)
        if articulo_form.is_valid():
            nombre = articulo_form.cleaned_data['nombre']
            marca = articulo_form.cleaned_data['marca']
            if Articulos.objects.filter(nombre=nombre, marca=marca).exists():
                mensaje_error = "Ya existe un artículo con ese nombre y marca."
            else:
                articulo_form.save()
                mensaje_exito = "¡Artículo agregado exitosamente!"
                articulo_form = ArticulosForm()
    else:
        articulo_form = ArticulosForm()
    return render(request, "AppCoder/articulos.html", {
        'articulo_form': articulo_form,
        'mensaje_exito': mensaje_exito,
        'mensaje_error': mensaje_error,
        'articulos': articulos,  # <-- Pasa la lista al template
    })

# Vista para mostrar el detalle de un artículo y contemplando el error 404 si no se encuentra
def articulo_detalle(request, pk):
    articulo = get_object_or_404(Articulos, pk=pk)
    return render(request, "AppCoder/articulo_detalle.html", {"articulo": articulo})

def registroUsuario(request):
    mensaje = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            # Normaliza email y username
            email_normalizado = informacion['email'].strip().lower() # Normaliza el email
            username_normalizado = informacion['username'].strip() # Normaliza el username
            # Validar si el email ya existe
            if Usuario.objects.filter(email__iexact=email_normalizado).exists():
                mensaje = "El email ya está registrado. Por favor, usa otro."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
            # Validar si el username ya existe
            if Usuario.objects.filter(username__iexact=username_normalizado).exists():
                mensaje = "El nombre de usuario ya está registrado. Por favor, elige otro."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
            # Intentar crear el usuario
            try:
                usuario = Usuario(
                    username=username_normalizado,
                    email=email_normalizado,
                    avatar=informacion.get('avatar', None)
                )
                usuario.set_password(informacion['password'])  # Hashea la contraseña correctamente
                usuario.save()
                mensaje = "¡Usuario registrado exitosamente!"
                return render(request, "AppCoder/registroUsuario.html", {'form': RegistroUsuarioForm(), 'mensaje': mensaje})
            # Intentar capturar errores de integridad
            except IntegrityError:
                mensaje = "El email ya está registrado. Por favor, usa otro."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
            # Capturar cualquier otro error inesperado
            except Exception:
                mensaje = "Ocurrió un error inesperado. Intenta con otros datos."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
        else:
            mensaje = "Por favor, revisa los datos ingresados."
    else:
        form = RegistroUsuarioForm()
    return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})

# Vista para manejar el login de usuarios
def login_usuario(request):
    mensaje = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].strip()
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('inicio')
            else:
                mensaje = "Usuario o contraseña incorrectos."
    else:
        form = LoginForm()
    return render(request, "AppCoder/login.html", {'form': form, 'mensaje': mensaje})

# Vista para que los usuarios editen sus propios datos
@login_required # Asegura que solo usuarios autenticados puedan acceder a esta vista
def mis_datos(request):
    usuario = request.user
    mensaje = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            mensaje = "¡Datos actualizados exitosamente!"
    else:
        form = RegistroUsuarioForm(instance=usuario)
    return render(request, "AppCoder/mis_datos.html", {'form': form, 'mensaje': mensaje})

# Vista para cambiar la contraseña del usuario autenticado
@login_required # Asegura que solo usuarios autenticados puedan acceder a esta vista
def cambiar_password(request):
    mensaje = None
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  # Esto usa set_password internamente
            update_session_auth_hash(request, user)  # Mantiene la sesión activa
            mensaje = "¡Contraseña cambiada exitosamente!"
            form = PasswordChangeForm(request.user)  # Limpia el formulario
        else:
            mensaje = "Por favor, corrige los errores abajo."
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "AppCoder/cambiar_password.html", {'form': form, 'mensaje': mensaje})