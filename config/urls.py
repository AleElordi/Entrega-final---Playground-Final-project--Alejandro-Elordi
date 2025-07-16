from django.urls import path, reverse_lazy # Importa reverse_lazy para redirección después de logout
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from AppCoder.templates.AppCoder.views.views import datos, resBusqueda, suscriptores, inicio, buscador, articulos, login_usuario, mis_datos, cambiar_password, articulo_detalle
from AppCoder.templates.AppCoder.views.usuarios import leerUsuarios, registroUsuario, eliminarUsuario, editarUsuario
from AppCoder.templates.AppCoder.views.productosRepuestos import articulosListView, articulosDetailView, articulosCreateView, articulosUpdateView, articulosDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('datos/', datos, name='datos'),
    path('suscriptores/', suscriptores, name='suscriptores'),
    path('buscador/', buscador, name='buscador'),
    path('resBuscador/', resBusqueda, name='resBusqueda'),
    path('articulos/', articulos, name='articulos'),
    path('articulos/<int:pk>/', articulo_detalle, name='articulo_detalle'),
    
    # Rutas para manejar usuarios
    path('usuarios/', leerUsuarios, name='usuarios'),
    path('registroUsuario/', registroUsuario, name='registroUsuario'),
    path('eliminarUsuario/<int:id>/', eliminarUsuario, name='eliminarUsuario'),
    path('editarUsuario/<int:id>/', editarUsuario, name='editarUsuario'),

    # Rutas para manejar productos y repuestos desde las vistas
    path('productosRepuestos/', articulosListView.as_view(), name='productosRepuestos_list'),
    path('productosRepuestos/<int:pk>/', articulosDetailView.as_view(), name='productosRepuestos_detail'),
    path('productosRepuestos/create/', articulosCreateView.as_view(), name='productosRepuestos_create'),
    path('productosRepuestos/update/<int:pk>/', articulosUpdateView.as_view(), name='productosRepuestos_update'),
    path('productosRepuestos/delete/<int:pk>/', articulosDeleteView.as_view(), name='productosRepuestos_delete'),
    
    # Rutas para el login de usuarios
    path('login/', login_usuario, name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('inicio')), name='logout'),

    #Rutas para el manejo de usuarios desde el admin
    path('usuarios_admin/', leerUsuarios, name='usuarios_admin'),
    path('usuarios_admin/editar/<int:id>/', editarUsuario, name='editar_usuario_admin'),
    path('usuarios_admin/eliminar/<int:id>/', eliminarUsuario, name='eliminar_usuario_admin'),
    path('mis-datos/', mis_datos, name='mis_datos'),
    path('cambiar-password/', cambiar_password, name='cambiar_password'),
]

# Rutas para manejar archivos multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)