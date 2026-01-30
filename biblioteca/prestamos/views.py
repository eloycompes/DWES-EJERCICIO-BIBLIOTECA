from django.shortcuts import render, get_object_or_404
from publicaciones.models import Unidad
from .models import Prestamo

# Create your views here.
def prestamos_unidad(request, unidad_id):
    unidad = get_object_or_404(Unidad, id=unidad_id)
    prestamos = unidad.prestamos.all()
    return render(request, 'prestamos/prestamos_unidad.html', {
        'unidad': unidad, 
        'prestamos': prestamos
    })