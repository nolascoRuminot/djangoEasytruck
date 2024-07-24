from django.forms import ModelForm
from .models import Tipo_usuario, Producto, Carrito, Ordene, Detalleordene

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['imagen', 'nombre', 'descripcion', 'preciouf', 'stock']