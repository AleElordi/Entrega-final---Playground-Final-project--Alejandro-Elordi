from django.shortcuts import render
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
# Esta vista se encarga de mostrar el formulario de registro y procesar los datos enviados por
def registroUsuario(request):
    mensaje = None
    if request.method == 'POST': # Verifico si el método de la petición es POST
        # Si es así, creo una instancia del formulario con los datos enviados
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