from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from apps.usuario.models import Propietario, Administrador, Veterinario
from apps.usuario.forms import PropietarioForm, VeterinarioForm, AdminForm


# Create your views here.

# PROPIETARIO
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

# VETERINARIO
class VeterinarioCreate(CreateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'Veterinario/veterinario_home.html'
    success_url = reverse_lazy('veterinario_listar')

class VeterinarioDelete(DeleteView):
    model = Veterinario
    template_name = 'Veterinario/veterinario_delete.html'
    success_url = reverse_lazy('veterinario_listar')

class VeterinarioDetail(DetailView):
    model = Veterinario
    template_name = 'Veterinario/veterinario_details.html'

class VeterinarioList(ListView):
    model = Veterinario
    template_name = 'Veterinario/veterinario_list.html'

class VeterinarioUpdate(UpdateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'Veterinario/veterinario_home.html'
    success_url = reverse_lazy('veterinario_listar')

# ADMINISTRADOR
class AdminCreate(CreateView):
    model = Administrador
    form_class = AdminForm
    template_name = 'Admin/admin_form.html'
    success_url = reverse_lazy('admin_listar')

class AdminDelete(DeleteView):
    model = Administrador
    template_name = 'Admin/admin_delete.html'
    success_url = reverse_lazy('admin_listar')

class AdminDetail(DetailView):
    model = Administrador
    template_name = 'Admin/admin_details.html'

class AdminList(ListView):
    model = Administrador
    template_name = 'Admin/admin_list.html'

class AdminUpdate(UpdateView):
    model = Administrador
    form_class = AdminForm
    template_name = 'Admin/admin_form.html'
    success_url = reverse_lazy('admin_listar')
