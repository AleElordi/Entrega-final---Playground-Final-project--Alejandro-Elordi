
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from AppCoder.models import Articulos


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
    fields = ['nombre', 'marca', 'foto', 'descripcion', 'precio', 'stock']
    template_name = 'AppCoder/productosRepuestos/productosRepuestos_form.html'

class articulosUpdateView(UpdateView):
    model = Articulos
    fields = ['nombre', 'marca', 'foto', 'descripcion', 'precio', 'stock']
    template_name = 'AppCoder/productosRepuestos/productosRepuestos_form.html'

class articulosDeleteView(DeleteView):
    model = Articulos
    template_name = 'AppCoder/productosRepuestos/productosRepuestos_confirm_delete.html'
