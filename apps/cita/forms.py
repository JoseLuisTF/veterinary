from django import forms

from apps.cita.models import CitaGeneral, HoraGeneral, CitaEstetica, Guarderia


class CitaGeneralForm(forms.ModelForm):
    class Meta:
        model = CitaGeneral
        fields = [
            'date',
            'time',
            'mascota',
            'informacion',
        ]
        labels = {
            'date': 'Fecha',
            'time': 'Horas Disponibles',
            'mascota': 'Mascota',
            'informacion': 'Informacion Adicional',
        }
        widgets = {
            'date': forms.Select(attrs={'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'mascota': forms.Select(attrs={'class': 'form-control'}),
            'informacion': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].queryset = HoraGeneral.objects.none()

        if 'date' in self.data:
            try:
                date_id = int(self.data.get('date'))
                self.fields['time'].queryset = HoraGeneral.objects.filter(date_id=date_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['time'].queryset = self.instance.especie.time_set


class CitaEsteticaForm(forms.ModelForm):
    class Meta:
        model = CitaEstetica
        fields = [
            'date',
            'time',
            'mascota',
            'informacion',
            'baño',
            'corte',
            'unias',
            'recoger'
        ]
        labels = {
            'date': 'Fecha',
            'time': 'Horas Disponibles',
            'mascota': 'Mascota',
            'informacion': 'Informacion Adicional',
            'baño': 'Servicio de Baño',
            'corte': 'Servicio de Corte de pelo',
            'unias': 'Servicio de Corte de uñas',
            'recoger': 'Servicio de Recogida en casa',

        }
        widgets = {
            'date': forms.Select(attrs={'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'mascota': forms.Select(attrs={'class': 'form-control'}),
            'informacion': forms.Textarea(attrs={'class': 'form-control'}),
            'baño': forms.CheckboxInput(),
            'corte': forms.CheckboxInput(),
            'unias': forms.CheckboxInput(),
            'recoger': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].queryset = HoraGeneral.objects.none()

        if 'date' in self.data:
            try:
                date_id = int(self.data.get('date'))
                self.fields['time'].queryset = HoraGeneral.objects.filter(date_id=date_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['time'].queryset = self.instance.especie.time_set


class GuarderiaForm(forms.ModelForm):
    class Meta:
        model = Guarderia
        fields = [
            'date_inicio',
            'date_fin',
            'mascota',
            'informacion',
            'recoger'
        ]
        labels = {
            'date_inicio': 'Fecha',
            'date_fin': 'Dia de Inicio',
            'mascota': 'Mascota',
            'informacion': 'Informacion Adicional',
            'recoger': 'Servicio de Recogida en casa',
        }
        widgets = {
            'date_inicio': forms.DateInput(attrs={'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control'}),
            'mascota': forms.Select(attrs={'class': 'form-control'}),
            'informacion': forms.Textarea(attrs={'class': 'form-control'}),
            'recoger': forms.CheckboxInput()
        }