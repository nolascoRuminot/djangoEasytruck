from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def servicios(request):
    return render(request, 'servicios.html')


def productos(request):
    return render(request, 'productos.html')

@login_required
def regProductosForm(request):
    return render(request, 'registrar-producto.html', {
        'form' : ProductoForm
    })

@login_required
def registrarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            new_producto = form.save(commit=False)
            new_producto.usuario = request.user  
            new_producto.save()
            return redirect('adminProd')  # Redirige a la vista de productos
        else:
            # Imprimir errores del formulario en la consola para depuración
            print(form.errors)
            return render(request, 'registrar-producto.html', {'form': form})  # Renderizar el formulario con errores si no es válido
    else:
        form = ProductoForm()
        return render(request, 'registrar-producto.html', {'form': form})

def clientes(request):
    return render(request, 'clientes.html')


def contacto(request):
    return render(request, 'contacto.html')


def carrito(request):
    return render(request, 'carrito.html')


def loginAdmin(request):
    return render(request, 'login-admin.html',{
        'form': AuthenticationForm
    })


def loginCliente(request):
    return render(request, 'login-cliente.html')

@login_required
def regCli(request):
    return render(request, 'registro-cliente.html')

@login_required
def admin(request):
    return render(request, 'administracion.html')

@login_required
def regAdmin(request):
    return render(request, 'registro-admin.html', {
        'form': UserCreationForm
    })

@login_required
def registrarAdmin(request):
    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create(
                username=request.POST['username'], password=request.POST['password1'])
            
            user.save()

            login(request, user)

            return render(request, 'login-admin.html', {
                'rgOk': '<p class="text-success">* Usuario creado</p>'
            })
        
        except IntegrityError:
            return render(request, 'registro-admin.html', {
                'form': UserCreationForm,
                'error': '* El usuario ya existe'
            })

    return render(request, 'registro-admin.html', {
                'form': UserCreationForm,
                'error': '* Contraseña no coinciden'
            })

def ingresar(request):
    user = authenticate(request, username = request.POST['username'], password=request.POST['password'])

    if user is None:
        return render(request, 'login-admin.html', {
                'form': AuthenticationForm,
                'eContr': '* Usuario y contraseña invalidos'
            })
    else:
        login(request, user)
        return redirect('adminProd')
    
@login_required
def adminProd(request):

    tProducto = Producto.objects.all()

    return render(request, 'admin-productos.html', {
        'tProducto': tProducto
    })

@login_required
def actProd(request, idProd):

    if request.method == 'GET':

        iProd = get_object_or_404(Producto, productoid=idProd)
        form = ProductoForm(instance=iProd)
        return render(request, 'actualizar-producto.html', {
            'iProd': iProd, 'form': form
        })
    
    else:

        try:
            iProd = get_object_or_404(Producto, productoid=idProd)
            form = ProductoForm(request.POST, instance=iProd)
            form.save()
            return redirect('adminProd')
        except ValueError:

            return render(request, 'actualizar-producto.html', {
            'iProd': iProd,
            'form': form, 
            'error': "Error al actualizar el producto"
        })

@login_required
def eliminarProd(request, idProd):
    iProd = get_object_or_404(Producto, productoid=idProd)
    iProd.delete()
    return redirect('adminProd')

def cerrarSesion(request):
    logout(request)
    return redirect('index')