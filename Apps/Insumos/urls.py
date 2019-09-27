from django.urls import path
from . import views

app_name = 'producto'
urlpatterns = [

    path('nuevoProducto/', (views.CrearProducto.as_view()), name='nuevoProducto'),
    path('listarProducto/', (views.ListarProductos.as_view()), name='listarProducto'),
    path('editarProducto/<int:pk>/', (views.EditarProducto.as_view()), name='editarProducto'),
    path('eliminarProducto/<int:pk>/', (views.EliminarProducto.as_view()), name='eliminarProducto'),
    path('detalleProducto/<int:pk>/', (views.DetalleProducto.as_view()), name='detalleProducto'),
]
