from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView


from apps.usuario.models import Veterinario, Profile
from apps.usuario.forms import ProfileForm


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.address = form.cleaned_data.get('address')
        user.profile.telephone = form.cleaned_data.get('telephone')
        user.profile.document = form.cleaned_data.get('document')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
    return render(request, 'signup.html', {'form': form})

# class PropietarioList(ListView):
#     model = Profile
#     template_name = 'Usuario/Propietario/propietario_list.html'


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'Usuario/Propietario/propietario_form.html'


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'Usuario/Propietario/propietario_details.html'


# # VETERINARIO
# class VeterinarioCreate(CreateView):
#     model = Veterinario
#     form_class = VeterinarioForm
#     template_name = 'Usuario/Veterinario/veterinario_home.html'
#     success_url = reverse_lazy('veterinario_listar')
#
#
# class VeterinarioDelete(DeleteView):
#     model = Veterinario
#     template_name = 'Usuario/Veterinario/veterinario_delete.html'
#     success_url = reverse_lazy('veterinario_listar')
#
#
# class VeterinarioDetail(DetailView):
#     model = Veterinario
#     template_name = 'Usuario/Veterinario/veterinario_details.html'
#
#
# class VeterinarioList(ListView):
#     model = Veterinario
#     template_name = 'Usuario/Veterinario/veterinario_list.html'
#
#
# class VeterinarioUpdate(UpdateView):
#     model = Veterinario
#     form_class = VeterinarioForm
#     template_name = 'Usuario/Veterinario/veterinario_home.html'
#     success_url = reverse_lazy('veterinario_listar')
