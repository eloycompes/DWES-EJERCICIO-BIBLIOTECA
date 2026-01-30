from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from biblioteca.publicaciones.models import Autor

# Create your views here.
class Autores_lista(ListView):
    model = Autor
    template_name = 'publicaciones/autores_lista.html'
    context_object_name = 'autores'

class Autor_detalle(DetailView):
    model = Autor
    template_name = 'publicaciones/autor_detalle.html'
    context_object_name = 'autor'

class Autor_crear(CreateView):
    model = Autor
    template_name = 'publicaciones/autor_crear.html'
    fields = ['nombre', 'apellido', 'fecha_nacimiento']
    success_url = reverse_lazy('autores-lista')