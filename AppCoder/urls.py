from django.urls import path
from .views import cursos, profesores, estudiantes, entregables, inicio 

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
]