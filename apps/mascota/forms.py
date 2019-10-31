from django import forms
from apps.mascota.models import Especie, Mascota, Raza


class MascotaForm (forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        labels = {
            'alias': 'Alias',
            'especie': 'Especie',
            'raza': 'Raza',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'propietario': 'Propietario',
        }
        widgets = {
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'raza': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
        }
