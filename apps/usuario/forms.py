from django import forms
from apps.usuario.models import Propietario, Administrador, Veterinario


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cc': 'Cédula',
            'clave': 'Contraseña',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'email': 'Correo Electrónico',
            'celular': 'Teléfono Celular',
            'fecha_nacimiento': 'Fecha Nacimiento',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'cc': forms.TextInput(attrs={'class': 'form-control'}),
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
        }


class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cc': 'Cédula',
            'clave': 'Contraseña',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'email': 'Correo Electrónico',
            'celular': 'Teléfono Celular',
            'fecha_nacimiento': 'Fecha Nacimiento',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'cc': forms.TextInput(attrs={'class': 'form-control'}),
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
        }


class AdminForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'
        labels = {
            'usuario': 'Usuario',
            'clave': 'Contraseña',
            'email': 'email',
        }
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }