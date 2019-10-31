from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDetail, MascotaDelete

urlpatterns = [
    path('listar', login_required(MascotaList.as_view()), name='mascota_listar'),
    path('agregar', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    path('actualizar/<pk>', login_required(MascotaUpdate.as_view()), name='mascota_actualizar'),
    path('detalles/<pk>', login_required(MascotaDetail.as_view()), name='mascota_detalles'),
    path('eliminar/<pk>', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
]