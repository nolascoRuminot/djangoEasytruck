from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('productos/', views.productos, name='productos'),
    path('clientes/', views.clientes, name='clientes'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('login-admin/', views.loginAdmin, name='logAdmin'),
    path('login-cliente/', views.loginCliente, name='logCliente'),
    path('registro-cliente/', views.regCli, name='regCliente'),
    
]