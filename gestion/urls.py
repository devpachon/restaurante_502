from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    #path('empleados/,', views.lista_empleados, name='lista_empleados'),
    path('mesas/', views.lista_mesas, name='lista_mesas'),
    path('platos/', views.lista_platos, name='lista_platos'),
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
    path('facturas/', views.lista_facturas, name='lista_facturas'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
]
