from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Autor
from .forms import AutorForm

# Create your views here.
class autores_lista(ListView):
    model = Autor
    template_name = 'publicaciones/autores_lista.html'
    context_object_name = 'autores'


class crear_autor(CreateView):
    model = Autor
    template_name = 'publicaciones/crear_autor.html'
    form_class = AutorForm
    success_url = '/publicaciones/autores/'