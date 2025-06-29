from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludar(request):
    """
    Vista que devuelve un saludo.
    """
    return HttpResponse("¡Hola, mundo!")