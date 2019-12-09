from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.http import HttpResponseRedirect

from apps.mascota.models import Mascota, Raza
from apps.mascota.forms import MascotaForm
from apps.usuario.models import Profile


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

    def get_queryset(self):
        return Mascota.objects.filter(propietario=self.request.user.profile)


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_listar')

    def form_valid(self, form):
        form.instance.propietario = self.request.user.profile
        return super(MascotaCreate, self).form_valid(form)


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota_listar')


class MascotaDetail(DetailView):
    model = Mascota
    template_name = 'mascota/mascota_details.html'


def load_razas(request):
    especie_id = request.GET.get('especie')
    razas = Raza.objects.filter(especie_id=especie_id)
    return render(request, 'mascota/razas_dropdown_list_options.html', {'razas': razas})
