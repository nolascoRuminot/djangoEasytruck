from django.shortcuts import render

# Create your views here.
def index(resquest):
    return render(resquest, 'easytruck/index.html')

def nosotros(resquest):
    return render(resquest, 'easytruck/nosotros.html')

def servicios(resquest):
    return render(resquest, 'easytruck/servicios.html')

def productos(resquest):
    return render(resquest, 'easytruck/productos.html')

def clientes(resquest):
    return render(resquest, 'easytruck/clientes.html')

def contacto(resquest):
    return render(resquest, 'easytruck/contacto.html')

def carrito(resquest):
    return render(resquest, 'easytruck/carrito.html')

def loginAdmin(resquest):
    return render(resquest, 'easytruck/login-admin.html')

def loginCli(resquest):
    return render(resquest, 'easytruck/login-cliente.html')

def regCli(resquest):
    return render(resquest, 'easytruck/registro-cliente.html')