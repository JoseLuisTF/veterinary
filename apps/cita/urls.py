from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required

from apps.cita.views import CitaGeneralCreate, CitaList, CitaAgendar, CitaEsteticaCreate, GuarderiaCreate

urlpatterns = [
    path('listar', CitaList.as_view(), name='listar'),
    path('agendar_general', CitaGeneralCreate.as_view(), name='general_agendar'),
    path('agendar_estetica', CitaEsteticaCreate.as_view(), name='estetica_agendar'),
    path('agendar_guarderia', GuarderiaCreate.as_view(), name='guarderia_agendar'),
    path('agendar', CitaAgendar.as_view(), name='agendar'),

    path('ajax/load-hours/', views.load_hours, name='ajax_load_hours')
]
