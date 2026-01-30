from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.fecha_nacimiento})"
    
class Autor(Persona):

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.fecha_nacimiento})"
    
class Unidad(models.Model):
    ESTADO = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
        ('muy_usado', 'Muy Usado'),
        ('a_retirar', 'A Retirar'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO, default='nuevo')

    def __str__(self):
        return f"Estado: {self.estado}"
    
class Publicacion(models.Model):
    TIPO_PUBLICACION = [
        ('libro', 'Libro'),
        ('articulo', 'Artículo'),
    ]
    tipo_publicacion = models.CharField(max_length=20, choices=TIPO_PUBLICACION, default='libro')
    ISBN = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    autor = models.ManyToManyField(Autor, related_name='publicaciones')
    fecha_publicacion = models.DateField()
    editorial = models.CharField(max_length=100)
    unidad = models.ManyToManyField(Unidad, related_name='publicaciones')

    def __str__(self):
        return f"{self.titulo} ({self.ISBN})"