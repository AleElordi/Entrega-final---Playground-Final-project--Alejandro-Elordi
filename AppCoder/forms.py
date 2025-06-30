from django import forms
from .models import Producto, Repuesto

class datosSuscriptor(forms.Form):
    nombreCompleto = forms.CharField(max_length=100, label="Nombre Completo")
    email = forms.EmailField(label="Email")
    fecha_suscripcion = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Fecha de Suscripción"
    )

#Creo las clases de los formularios para Producto y Repuesto utilizando ModelForm y no el Form
#con esto puedo utilizar los atributos de los modelos directamente y no tengo que definirlos manualmente
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = '__all__'