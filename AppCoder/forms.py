from django import forms

class datosSuscriptor(forms.Form):
    nombreCompleto = forms.CharField(max_length=100, label="Nombre Completo")
    email = forms.EmailField(label="Email")
    fecha_suscripcion = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Fecha de Suscripción"
    )