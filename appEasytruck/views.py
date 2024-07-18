from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


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

def admin(resquest):
    return render(resquest, 'administracion.html')


def regAdmin(resquest):
    return render(resquest, 'registro-admin.html', {
        'form': UserCreationForm
    })


def registrarCli(resquest):
    if resquest.POST['password1'] == resquest.POST['password2']:
        try:
            user = User.objects.create(
                username=resquest.POST['username'], password=resquest.POST['password'])
            
            user.save()

            login(resquest, user)

            return render(resquest, 'login-admin.html', {
                'mnsj': '<p class="text-success">* Usuario creado</p>'
            })
        
        except IntegrityError:
            return render(resquest, 'registro-admin.html', {
                'form': UserCreationForm,
                'error': '* El usuario ya existe'
            })

    return render(resquest, 'registro-admin.html', {
                'form': UserCreationForm,
                'error': '* Contraseña no coinciden'
            })
