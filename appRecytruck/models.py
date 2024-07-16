from django.db import models

# Create your models here.

class Tipo_usuario(models.Model):
    
    tipousuarioid = models.AutoField(primary_key=True)
    nombretipo = models.CharField(max_length=50)
   
    def __str__(self) :
        return str(self.tipousuarioid) + " " + str(self.nombretipo)

class Usuario(models.Model):

    usuarioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    passwordhash = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    tipousuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE, db_column='tipousuarioid')

    def __str__(self) :
        return str(self.usuarioid) + " " + str(self.nombre) + " " + str(self.apellido) + " " + str(self.email) + " " + str(self.passwordhash) + " " + str(self.fechacreacion) + " " + str(self.tipousuario)

class Cliente(models.Model):
    
    clienteid = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(max_length=50)
    apellidoCliente = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    emailCliente = models.CharField(max_length=50)
    passwordhashCliente = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)

    def __str__(self) :
        return str(self.clienteid) + " " + str(self.nombreCliente) + " " + str(self.apellidoCliente) + " " + str(self.empresa) + " " + str(self.emailCliente) + " " + str(self.passwordhashCliente) + " " + str(self.direccion) + " " + str(self.telefono)
      
class Producto(models.Model):
    
    productoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.CharField(max_length=10)
    stock = models.CharField(max_length=10)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    usuarioid = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuarioid')

    def __str__(self) :
        return str(self.productoid) + " " + str(self.nombre) + " " + str(self.descripcion) + " " + str(self.precio) + " " + str(self.stock) + " " + str(self.fechacreacion)

class Carrito(models.Model):
    
    carritoid = models.AutoField(primary_key=True)
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='productoid')
    precio = models.CharField(max_length=10)
    cantidad = models.CharField(max_length=10)
    totalvalorprod = models.CharField(max_length=10)
    subtotal = models.CharField(max_length=10)
    iva = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='clienteid')
    fechacreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.carritoid) + " " + str(self.productoid) + " " + str(self.precio) + " " + str(self.cantidad) + " " + str(self.totalvalorprod) + " " + str(self.subtotal) + " " + str(self.iva) + " " + str(self.total) + " " + str(self.clienteid) + " " + str(self.fechacreacion)
    
class Ordene(models.Model):
    
    ordenid = models.AutoField(primary_key=True)
    fechaorden = models.DateTimeField(auto_now_add=True)
    clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='clienteid')
    subtotal = models.CharField(max_length=10)
    iva = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='clienteid')
    estado = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.ordenid) + " " + str(self.fechaorden) + " " + str(self.clienteid) + " " + str(self.subtotal) + " " + str(self.iva) + " " + str(self.total) + " " + str(self.clienteid) + " " + str(self.estado)
    
class Detalleordene(models.Model):
    
    detalleid = models.AutoField(primary_key=True)
    ordenid = models.ForeignKey(Ordene, on_delete=models.CASCADE, db_column='ordenid')
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='productoid')
    precio = models.CharField(max_length=10)
    cantidad = models.CharField(max_length=10)
    totalvalorprod = models.CharField(max_length=10)

    def __str__(self) :
        return str(self.detalleid) + " " + str(self.ordenid) + " " + str(self.productoid) + " " + str(self.precio) + " " + str(self.cantidad) + " " + str(self.totalvalorprod)
    
