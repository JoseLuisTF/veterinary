from django.contrib import admin
from apps.usuario.models import Profile, Veterinario

# Register your models here.
admin.site.register(Profile)
admin.site.register(Veterinario)
