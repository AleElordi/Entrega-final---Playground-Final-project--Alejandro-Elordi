from django import forms
from .models import Producto, Repuesto, Articulos, Usuario

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
        model = Articulos  # Asumiendo que Articulos es un modelo similar a Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# Creo la clase de formulario para el registro de usuarios con avatar propio
class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# Validación personalizada para el campo username
def clean_username(self):
    username = self.cleaned_data.get('username')
    if len(username) < 4:
        raise forms.ValidationError("El nombre de usuario debe tener al menos 4 caracteres.")
    return username
    
# Creo la clase de formulario para el inicio de sesión
class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))