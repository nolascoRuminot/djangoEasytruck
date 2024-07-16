from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


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

def loginCli(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página de inicio u otra página
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'easytruck/login-cliente.html', {'form': form})


def regCli(resquest):
    return render(resquest, 'easytruck/registro-cliente.html')