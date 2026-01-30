from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.Autores_lista.as_view(), name='autores-lista'),
    path('autores/crear/', views.Autor_crear.as_view(), name='autor-crear'),
    path('autores/<int:pk>/', views.Autor_detalle.as_view(), name='autor-detalle'),
]