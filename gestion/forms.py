from django import forms
from .models import Cliente


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