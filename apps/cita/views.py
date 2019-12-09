from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy

from apps.cita.models import CitaGeneral, HoraGeneral, Fecha, CitaEstetica, Guarderia
from apps.cita.forms import CitaGeneralForm, CitaEsteticaForm, GuarderiaForm


# Create your views here.

class CitaAgendar(TemplateView):
    template_name = 'cita/cita_agendar.html'


class CitaGeneralCreate(CreateView):
    model = CitaGeneral
    form_class = CitaGeneralForm
    template_name = 'cita/cita_general_form.html'
    success_url = reverse_lazy('listar')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.tipo_cita = 'Cita General'
        HoraGeneral.objects.filter(pk=form.instance.time.pk).update(ocupado=True)
        return super(CitaGeneralCreate, self).form_valid(form)


class CitaEsteticaCreate(CreateView):
    model = CitaEstetica
    form_class = CitaEsteticaForm
    template_name = 'cita/cita_general_form.html'
    success_url = reverse_lazy('listar')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.tipo_cita = 'Cita Estetica'
        HoraGeneral.objects.filter(pk=form.instance.time.pk).update(ocupado=True)
        return super(CitaEsteticaCreate, self).form_valid(form)


class GuarderiaCreate(CreateView):
    model = Guarderia
    form_class = GuarderiaForm
    template_name = 'cita/cita_general_form.html'
    success_url = reverse_lazy('listar')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.tipo_cita = 'Guarderia'
        return super(GuarderiaCreate, self).form_valid(form)


class CitaList(TemplateView):
    template_name = 'cita/cita_list.html'

    def get_context_data(self, *args, **kwargs):
        generales = CitaGeneral.objects.filter(profile=self.request.user.profile)
        esteticas = CitaEstetica.objects.filter(profile=self.request.user.profile)
        guarderias = Guarderia.objects.filter(profile=self.request.user.profile)
        return {'generales': generales, 'esteticas': esteticas, 'guarderias': guarderias}


def load_hours(request):
    date_id = request.GET.get('date')
    hours = HoraGeneral.objects.filter(date_id=date_id, ocupado=False)
    return render(request, 'cita/hours_dropdown_list_options.html', {'hours': hours})
