from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def saludar(request):
    """
    Vista que devuelve un saludo.
    """
    return HttpResponse("¡Hola, mundo!")

def index(request):
    """
    Vista que renderiza la plantilla index.html.
    """
    return render(request, 'core/index.html')

def current_datetime(request):
    """
    Vista que devuelve la fecha y hora actual.
    """
    now = datetime.now()

    html = {
        'current_time': now,
        'title': 'Fecha y Hora Actual',
        'description': 'Esta es una página que muestra la fecha y hora actual.',    
    }

    return render(request, 'core/current_datetime.html', html)