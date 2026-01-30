from django.db import models

# Create your models here.
class Unidad(models.Model):
    ESTADO = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
        ('muy_usado', 'Muy Usado'),
        ('a_retirar', 'A retirar'),
    ]

    estado = models.CharField(max_length=20, choices=ESTADO)

    def __str__(self):
        return self.estado
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Publicacion(models.Model):
    TIPO_PUBLICACION = [
        ('libro', 'Libro'),
        ('articulo', 'Artículo'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_PUBLICACION)
    ISBN = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    autor = models.ManyToManyField(Autor, related_name='publicaciones')
    unidades = models.ManyToManyField(Unidad, related_name='publicaciones')
    editorial = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} ({self.ISBN})"