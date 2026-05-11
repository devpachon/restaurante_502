from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ClienteForm
from .forms import EmpleadoForm
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura

@login_required
def inicio(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_empleados': Empleado.objects.count(),
        'total_mesas': Mesa.objects.count(),
        'total_platos': Plato.objects.count(),
        'total_ordenes': Orden.objects.count(),
        'total_facturas': Factura.objects.count(),
    }
    return render(request, 'gestion/inicio.html', context)

@login_required
def lista_clientes(request):

    clientes = Cliente.objects.all()
    return render(request, 'gestion/clientes.html', {'clientes': clientes})

@login_required
def crear_cliente(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista_clientes')

    else:

        form = ClienteForm()

    return render(
        request,
        'gestion/form_cliente.html',
        {
            'form': form,
            'titulo': 'Crear Cliente'
        }
    )

@login_required
def editar_cliente(request, id):

    cliente = get_object_or_404(
        Cliente,
        id=id
    )

    if request.method == 'POST':

        form = ClienteForm(
            request.POST,
            instance=cliente
        )

        if form.is_valid():

            form.save()

            return redirect('lista_clientes')

    else:

        form = ClienteForm(
            instance=cliente
        )

    return render(
        request,
        'gestion/form_cliente.html',
        {
            'form': form,
            'titulo': 'Editar Cliente'
        }
    )

@login_required
def eliminar_cliente(request, id):

    cliente = get_object_or_404(
        Cliente,
        id=id
    )

    cliente.delete()

    return redirect('lista_clientes')

@login_required
def lista_empleados(request):

    empleados = Empleado.objects.all()
    return render(request, 'gestion/empleados.html', {'empleados': empleados})

@login_required
def crear_empleado(request):

    if request.method == 'POST':

        form = EmpleadoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista_empleados')

    else:

        form = EmpleadoForm()

    return render(
        request,
        'gestion/form_empleado.html',
        {
            'form': form,
            'titulo': 'Crear Empleado'
        }
    )

@login_required
def editar_empleado(request, id):

    empleado = get_object_or_404(
        Empleado,
        id=id
    )

    if request.method == 'POST':

        form = EmpleadoForm(
            request.POST,
            instance=empleado
        )

        if form.is_valid():

            form.save()

            return redirect('lista_empleados')

    else:

        form = EmpleadoForm(
            instance=empleado
        )

    return render(
        request,
        'gestion/form_empleado.html',
        {
            'form': form,
            'titulo': 'Editar Empleado'
        }
    )

@login_required
def eliminar_empleado(request, id):

    empleado = get_object_or_404(
        Empleado,
        id=id
    )

    empleado.delete()

    return redirect('lista_empleados')

@login_required
def lista_mesas(request):

    mesas = Mesa.objects.all()
    return render(request, 'gestion/mesas.html', {'mesas': mesas})

@login_required
def lista_platos(request):

    platos = Plato.objects.all()
    return render(request, 'gestion/platos.html', {'platos': platos})

@login_required
def lista_ordenes(request):

    ordenes = Orden.objects.all()
    return render(request, 'gestion/ordenes.html', {'ordenes': ordenes})

@login_required
def lista_facturas(request):

    facturas = Factura.objects.all()
    return render(request, 'gestion/facturas.html', {'facturas': facturas})

def login_view(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('inicio')

        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'gestion/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

