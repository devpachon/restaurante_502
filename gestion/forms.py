from django import forms
from .models import Cliente
from .models import Empleado


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