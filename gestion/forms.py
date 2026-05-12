from django import forms
from .models import Cliente
from .models import Empleado
from .models import Mesa
from .models import Plato
from .models import Orden, DetalleOrden


class ClienteForm(forms.ModelForm):

    class Meta:

        model = Cliente

        fields = [
            'nombre',
            'telefono',
            'correo'
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

        }

class EmpleadoForm(forms.ModelForm):

    class Meta:

        model = Empleado

        fields = [
            'nombre',
            'cargo',
            'telefono',
            'correo'
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'cargo': forms.Select(attrs={
                'class': 'form-control'
            }),

            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

        }

class MesaForm(forms.ModelForm):

    class Meta:

        model = Mesa

        fields = [
            'numero_mesa',
            'capacidad',
            'estado_mesa'
        ]

        widgets = {

            'numero_mesa': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'capacidad': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'estado_mesa': forms.Select(attrs={
                'class': 'form-control'
            }),

        }

class PlatoForm(forms.ModelForm):

    class Meta:

        model = Plato

        fields = [
            'nombre_plato',
            'descripcion',
            'precio',
            'categoria',
            'disponible'
        ]

        widgets = {

            'nombre_plato': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'categoria': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),

        }

class OrdenForm(forms.ModelForm):

    class Meta:

        model = Orden

        fields = [
            'cliente',
            'empleado',
            'mesa',
            'estado_orden'
        ]

        widgets = {

            'cliente': forms.Select(attrs={
                'class': 'form-control'
            }),

            'empleado': forms.Select(attrs={
                'class': 'form-control'
            }),

            'mesa': forms.Select(attrs={
                'class': 'form-control'
            }),

            'estado_orden': forms.Select(attrs={
                'class': 'form-control'
            }),

        }

class DetalleOrdenForm(forms.ModelForm):

    class Meta:

        model = DetalleOrden

        fields = [
            'plato',
            'cantidad'
        ]

        widgets = {

            'plato': forms.Select(attrs={
                'class': 'form-control'
            }),

            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

        }