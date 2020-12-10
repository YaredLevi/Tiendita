from django.urls import path
from .views import listado_productos, read, agregar, eliminar

urlpatterns = [
    path('', listado_productos, name='listado_productos'),
    path('products/read/', read, name='read'),
    path('products/agregar/', agregar, name='agregar'),
    path('products/eliminar/<id>/', eliminar, name='eliminar')
]
