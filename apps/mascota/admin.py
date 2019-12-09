from django.contrib import admin
from apps.mascota.models import Raza, Especie, Mascota

# Register your models here.
admin.site.register(Raza)
admin.site.register(Especie)
admin.site.register(Mascota)
