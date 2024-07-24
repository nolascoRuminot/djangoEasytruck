from django.contrib import admin
from .models import Tipo_usuario, Producto, Carrito, Ordene, Detalleordene

# Register your models here.
admin.site.register(Tipo_usuario)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Ordene)
admin.site.register(Detalleordene)

