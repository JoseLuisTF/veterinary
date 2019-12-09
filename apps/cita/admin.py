from django.contrib import admin
from apps.cita.models import Fecha, HoraGeneral, CitaGeneral

# Register your models here.
admin.site.register(Fecha)
admin.site.register(HoraGeneral)
admin.site.register(CitaGeneral)
