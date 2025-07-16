from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect # Importar funciones de Django que permiten renderizar templates y manejar objetos
from AppCoder.models import Usuario
from AppCoder.forms import RegistroUsuarioForm

# Vista para mostrar todos los usuarios registrados
# Esta vista se encarga de recuperar todos los usuarios de la base de datos y pasarlos
def leerUsuarios(request):
    usuarios = Usuario.objects.all() #traigo todos los usuarios de la base de datos
    contexto = {
        "usuarios": usuarios #paso los usuarios al contexto para que se puedan mostrar en el template
    }
    return render(request, "AppCoder/usuarios.html", contexto)

# Vista para registrar un nuevo usuario
def registroUsuario(request):
    mensaje = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            email_normalizado = informacion['email'].strip().lower()
            username_normalizado = informacion['username'].strip()
            # Validar si el email ya existe
            if Usuario.objects.filter(email__iexact=email_normalizado).exists():
                mensaje = "El email ya está registrado. Por favor, usa otro."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
            # Validar si el username ya existe
            if Usuario.objects.filter(username__iexact=username_normalizado).exists():
                mensaje = "El nombre de usuario ya está registrado. Por favor, elige otro."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
            # Crear el usuario y hashear la contraseña
            try:
                usuario = Usuario(
                    username=username_normalizado,
                    email=email_normalizado,
                    avatar=informacion.get('avatar', None)
                )
                usuario.set_password(informacion['password'])  # Hashea la contraseña
                usuario.save()
                mensaje = "¡Usuario registrado exitosamente!"
                return render(request, "AppCoder/registroUsuario.html", {'form': RegistroUsuarioForm(), 'mensaje': mensaje})
            except IntegrityError:
                mensaje = "El email ya está registrado. Por favor, usa otro."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
            except Exception:
                mensaje = "Ocurrió un error inesperado. Intenta con otros datos."
                return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})
        else:
            mensaje = "Por favor, revisa los datos ingresados."
    else:
        form = RegistroUsuarioForm()
    return render(request, "AppCoder/registroUsuario.html", {'form': form, 'mensaje': mensaje})


# Vista para eliminar un usuario por su ID
# Esta vista se encarga de eliminar un usuario de la base de datos y mostrar un mensaje
def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)  # Obtengo el usuario por su ID
    usuario.delete()  # Elimino el usuario de la base de datos
    return render(request, "AppCoder/usuarios.html", {"mensaje": "Usuario eliminado exitosamente."})


def editarUsuario(request, id):
    mensaje = None
    usuario = Usuario.objects.get(id=id)  # Obtengo el usuario por su ID
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST) # Formulario con los datos del usuario
        # Verifico si el formulario es válido
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.avatar = informacion.get('avatar', None)
            # No actualizo la contraseña aquí, ya que es un campo sensible            
            usuario.save()  # Actualizo el usuario con los datos del formulario
            mensaje = "¡Usuario editado exitosamente!"
            return leerUsuarios(request)  # Redirijo a la lista de usuarios después de editar
    else:
        form = RegistroUsuarioForm(
            initial={
                'username': usuario.username,
                'email': usuario.email,
                'avatar': usuario.avatar
            }
            )  # Formulario con los datos del usuario
    
    return render(request, "AppCoder/editarUsuario.html", {'form': form, 'usuario': usuario.id, 'mensaje': mensaje})


# Solo permite acceso a superusuarios (admin)
def admin_required(user):
    return user.is_superuser

# Decorador para restringir el acceso a la vista de usuarios
# Solo los usuarios que cumplen con el admin_required pueden acceder a esta vista
@user_passes_test(admin_required)
def leerUsuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        "usuarios": usuarios
    }
    return render(request, "AppCoder/usuarios.html", contexto)

# Decoradores para restringir el acceso a las vistas de edición y eliminación de usuarios
# Solo los usuarios que cumplen con el admin_required pueden acceder a estas vistas
@user_passes_test(admin_required)
def eliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        usuario.delete()
        return redirect('usuarios_admin')
    return render(request, "AppCoder/eliminarUsuario.html", {"usuario": usuario})

# Decorador para restringir el acceso a la vista de edición de usuarios
# Solo los usuarios que cumplen con el admin_required pueden acceder a esta vista
@user_passes_test(admin_required)
def editarUsuario(request, id):
    mensaje = None
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            try:
                form.save()
                mensaje = "¡Usuario editado exitosamente!"
                return redirect('usuarios_admin')
            except IntegrityError:
                mensaje = "El email ya está registrado. Por favor, usa otro."
    else:
        form = RegistroUsuarioForm(instance=usuario)
    return render(request, "AppCoder/editarUsuario.html", {'form': form, 'usuario': usuario, 'mensaje': mensaje})