from django import forms
from apps.mascota.models import Mascota, Raza


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'alias',
            'especie',
            'raza',
            'edad',
            'sexo',
            'imagen'
        ]
        labels = {
            'alias': 'Alias',
            'especie': 'Especie',
            'raza': 'Raza',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'imagen': 'Foto',
        }
        widgets = {
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'raza': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['raza'].queryset = Raza.objects.none()

        if 'especie' in self.data:
            try:
                especie_id = int(self.data.get('especie'))
                self.fields['raza'].queryset = Raza.objects.filter(especie_id=especie_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['raza'].queryset = self.instance.especie.raza_set.order_by('nom_raza')
