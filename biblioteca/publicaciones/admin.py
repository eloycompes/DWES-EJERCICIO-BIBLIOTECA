from django.contrib import admin
from .models import Unidad, Autor, Publicacion

# Register your models here.
admin.site.register(Unidad)
admin.site.register(Autor)
admin.site.register(Publicacion)