from django.shortcuts import render
from django.views.generic import ListView
from biblioteca.publicaciones.models import Autor

# Create your views here.
class autores_lista(ListView):
    model = Autor
    template_name = 'publicaciones/autores_lista.html'
    context_object_name = 'autores'