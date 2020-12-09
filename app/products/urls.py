from django.urls import path
from .views import listado_productos, read, agregar

urlpatterns = [
    path('', listado_productos, name='listado_productos'),
    path('products/read/', read, name='read'),
    path('products/agregar/', agregar, name='agregar'),
]
