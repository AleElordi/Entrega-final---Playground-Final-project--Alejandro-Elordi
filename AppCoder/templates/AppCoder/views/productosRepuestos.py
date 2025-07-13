
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from AppCoder.models import Articulos
from django.urls import reverse_lazy # Importante para redirección después de eliminar un artículo
from AppCoder.forms import ArticulosForm

#Creo las vistas para manejar los productos y repuestos

#Creo las vistas para manejar los productos

class articulosListView(ListView):
    model = Articulos
    template_name = 'AppCoder/productosRepuestos/productosRepuestos_list.html'
    paginate_by = 10  # Número de artículos por página
    ordering = ['nombre',]  # Ordenar por nombre de artículo

class articulosDetailView(DetailView):
    model = Articulos
    template_name = 'AppCoder/productosRepuestos/productosRepuestos_detail.html'

class articulosCreateView(CreateView):
    model = Articulos
    form_class = ArticulosForm # Formulario para crear un nuevo artículo
    template_name = 'AppCoder/productosRepuestos/productosRepuestos_form.html'

class articulosUpdateView(UpdateView):
    model = Articulos
    form_class = ArticulosForm # Formulario para actualizar un artículo existente
    template_name = 'AppCoder/productosRepuestos/productosRepuestos_form.html'

class articulosDeleteView(DeleteView):
    model = Articulos
    template_name = "AppCoder/productosRepuestos/productosRepuestos_confirm_delete.html"
    success_url = reverse_lazy('productosRepuestos_list')  # reverse_lazy permite redirigir a la lista de artículos después de eliminar uno