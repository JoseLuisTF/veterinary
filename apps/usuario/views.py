from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from apps.usuario.models import Propietario, Administrador, Veterinario
from apps.usuario.forms import PropietarioForm, VeterinarioForm


# Create your views here.
class PropietarioCreate(CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'Propietario/propietario_home.html'
    success_url = reverse_lazy('propietario_listar')

class PropietarioList(ListView):
    model = Propietario
    template_name = 'Propietario/propietario_list.html'

class PropietarioDelete(DeleteView):
    model = Propietario
    template_name = 'Propietario/propietario_delete.html'
    success_url = reverse_lazy('propietario_listar')

class PropietarioUpdate(UpdateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'Propietario/propietario_home.html'
    success_url = reverse_lazy('propietario_listar')

class PropietarioDetail(DetailView):
    model = Propietario
    template_name = 'Propietario/propietario_details.html'

class VeterinarioCreate(CreateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'Veterinario/veterinario_home.html'
    success_url = reverse_lazy('veterinario_listar')

class VeterinarioDelete(DeleteView):
    model = Veterinario
    template_name = 'Veterinario/veterinario_delete.html'
    success_url = reverse_lazy('veterinario_listar')

class VeterinarioList(ListView):
    model = Veterinario
    template_name = 'Veterinario/veterinario_list.html'