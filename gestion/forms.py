from django import forms
from .models import Cliente
from .models import Empleado
from .models import Mesa


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