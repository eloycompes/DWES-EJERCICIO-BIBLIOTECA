from django.urls import path
from .views import prestamos_unidad

urlpatterns = [
    path('<int:unidad_id>/', prestamos_unidad, name='prestamos_unidad'),
]