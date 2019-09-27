from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import ProductoForm
from .models import Producto
from django.views import generic


# Create your views here.

# Clases del modulo de productos....................................


class CrearProducto(generic.CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:listarProducto')


class EditarProducto(generic.UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/editar.html'
    success_url = reverse_lazy('producto:listarProducto')


class ListarProductos(generic.ListView):
    model = Producto
    template_name = 'producto/listar.html'
    context_object_name = 'Productos'
    queryset = Producto.objects.all


class EliminarProducto(generic.DeleteView):
    model = Producto
    success_url = reverse_lazy('producto:listarProducto')


class DetalleProducto(generic.DeleteView):
    model = Producto
    template_name = 'producto/mostrar.html'
    queryset = Producto.objects.all

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Producto, id=id_)
