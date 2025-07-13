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

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Producto  # Asumiendo que Articulos es un modelo similar a Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),  # Campo adicional para tipo de artículo
            'foto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# Creo la clase de formulario para el registro de usuarios con avatar propio
class RegistroUsuarioForm(forms.Form):
    username = forms.CharField(max_length=150, label="Nombre de Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    email = forms.EmailField(label="Email")
    avatar = forms.ImageField(required=False, label="Avatar")

    # Validación personalizada para el campo username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError("El nombre de usuario debe tener al menos 4 caracteres.")
        return username