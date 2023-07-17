# Django

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)
# local
from applications.venta.models import SaleDetail
#
from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    template_name = "producto/lista.html"
    context_object_name = 'productos'

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Product.objects.buscar_producto(kword, order)
        return queryset



class ProductCreateView(CreateView):
    template_name = "producto/form_producto.html"
    form_class = ProductForm
    success_url = reverse_lazy('producto_app:producto-lista')


class ProductUpdateView(UpdateView):
    template_name = "producto/form_producto.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('producto_app:producto-lista')



class ProductDeleteView(DeleteView):
    template_name = "producto/delete.html"
    model = Product
    success_url = reverse_lazy('producto_app:producto-lista')


class ProductDetailView(DetailView):
    template_name = "producto/detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        context["ventas_mes"] = SaleDetail.objects.ventas_mes_producto(
            self.kwargs['pk']
        )
        return context



    

