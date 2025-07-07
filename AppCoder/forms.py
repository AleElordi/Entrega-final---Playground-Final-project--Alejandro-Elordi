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
        # crep widgets para que se vean bonitos en el HTML dando estilos a los campos del formulario con bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = '__all__'
        # crep widgets para que se vean bonitos en el HTML dando estilos a los campos del formulario con bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }