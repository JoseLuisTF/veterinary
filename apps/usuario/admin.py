from django.contrib import admin
from apps.usuario.models import Propietario,Veterinario,Administrador

# Register your models here.
admin.site.register(Propietario)
admin.site.register(Veterinario)
admin.site.register(Administrador)