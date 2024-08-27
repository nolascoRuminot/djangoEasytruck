from django.db import models
from django.contrib.auth.models import User
import os
import uuid


def generate_unique_filename(instance, filename):
    extension = filename.split('.')[-1]  
    new_filename = f"{uuid.uuid4()}.{extension}" 
    return os.path.join('img/productos/', new_filename)  

class Tipo_usuario(models.Model):
    tipousuarioid = models.AutoField(primary_key=True)
    nombretipo = models.CharField(max_length=50)
   
    def __str__(self):
        return str(self.tipousuarioid) + " " + str(self.nombretipo)

class Producto(models.Model):
    productoid = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to=generate_unique_filename)  # Usar la función personalizada para nombres únicos
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    preciouf = models.CharField(max_length=10)
    stock = models.IntegerField(default=1)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.productoid} {self.imagen} {self.nombre} {self.descripcion} {self.preciouf} {self.stock} {self.fechacreacion} {self.usuario}'

class Carrito(models.Model):
    carritoid = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='productoid')
    precio = models.CharField(max_length=10)
    cantidad = models.CharField(max_length=10)
    totalvalorprod = models.CharField(max_length=10)
    subtotal = models.CharField(max_length=10)
    iva = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fechacreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.carritoid} {self.producto} {self.precio} {self.cantidad} {self.totalvalorprod} {self.subtotal} {self.iva} {self.total} {self.fechacreacion}'

class Ordene(models.Model):
    ordenid = models.AutoField(primary_key=True)
    fechaorden = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.CharField(max_length=10)
    iva = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ordenid} {self.fechaorden} {self.usuario} {self.subtotal} {self.iva} {self.total} {self.estado}'

class Detalleordene(models.Model):
    detalleid = models.AutoField(primary_key=True)
    ordenid = models.ForeignKey(Ordene, on_delete=models.CASCADE, db_column='ordenid')
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='productoid')
    precio = models.CharField(max_length=10)
    cantidad = models.CharField(max_length=10)
    totalvalorprod = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.detalleid} {self.ordenid} {self.productoid} {self.precio} {self.cantidad} {self.totalvalorprod}'
