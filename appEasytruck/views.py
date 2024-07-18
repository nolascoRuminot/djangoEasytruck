from django.shortcuts import render

# Create your views here.

def index(resquest):
    return render(resquest, 'index.html')

def nosotros(resquest):
    return render(resquest, 'nosotros.html')

def servicios(resquest):
    return render(resquest, 'servicios.html')

def productos(resquest):
    return render(resquest, 'productos.html')

def clientes(resquest):
    return render(resquest, 'clientes.html')

def contacto(resquest):
    return render(resquest, 'contacto.html')

def carrito(resquest):
    return render(resquest, 'carrito.html')

def loginAdmin(resquest):
    return render(resquest, 'login-admin.html')

def loginCliente(resquest):
    return render(resquest, 'login-cliente.html')

def regCli(resquest):
    return render(resquest, 'registro-cliente.html')