from django import forms
from apps.usuario.models import Propietario, Administrador, Veterinario


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        labels = {
            'cc': 'Cédula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'clave': 'Contraseña',
            'sexo': 'Sexo',
            'celular': 'Teléfono Celular',
            'email': 'Correo Electrónico',
            'edad': 'Edad'
        }
        widgets = {
            'cc': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
        }


class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'
        labels = {
            'cc': 'Cédula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'clave': 'Contraseña',
            'sexo': 'Sexo',
            'celular': 'Teléfono Celular',
            'email': 'Correo Electrónico',
            'edad': 'Edad'
        }
        widgets = {
            'cc': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
        }
