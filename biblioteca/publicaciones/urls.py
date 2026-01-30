from django.urls import include, path
from . import views

urlpatterns = [
    path('autores/', views.autores_lista.as_view(), name='autores_lista'),
]