from django.db import models

# Create your models here.
class Prestamo(models.Model):
    unidad = models.ForeignKey('publicaciones.Unidad', on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    usuario = models.CharField(max_length=100)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"Préstamo de {self.unidad} a {self.usuario} el {self.fecha_prestamo}"