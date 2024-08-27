from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('productos/', views.productos, name='productos'),
    path('registrar-producto-form/', views.regProductosForm, name='regPrdFrm'),
    path('registrar-producto/', views.registrarProducto, name='regPrd'),
    path('clientes/', views.clientes, name='clientes'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('login-admin/', views.loginAdmin, name='logAdmin'),
    path('login-cliente/', views.loginCliente, name='logCliente'),
    path('registro-cliente/', views.regCli, name='regCliente'),
    path('registro-admin/', views.regAdmin, name='regAdmin'),
    path('registrar/', views.registrarAdmin, name='registrar'),
    path('admin/', views.registrarAdmin, name='admin'),
    path('cerrar-sesion/', views.cerrarSesion, name='cSesion'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('admin-productos/', views.adminProd, name='adminProd'),
    path('update-producto/<int:idProd>/', views.actProd, name='actProd'),
    path('eliminar-producto/<int:idProd>/', views.eliminarProd, name='elimProd'),
    path('cerrar-sesion/', views.cerrarSesion, name='cerrarSesion'),
    path('crear-administrador/', views.registrarAdmin, name='addAdmin'),
    

]