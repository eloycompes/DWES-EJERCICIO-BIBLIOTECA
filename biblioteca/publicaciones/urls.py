from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.autores_lista.as_view(), name='autores_lista'),
    path('autores/crear/', views.crear_autor.as_view(), name='crear_autor'),
]