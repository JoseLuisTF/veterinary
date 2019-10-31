from django.urls import path
from apps.usuario.views import PropietarioCreate, PropietarioList, PropietarioDelete, PropietarioUpdate, PropietarioDetail, \
    VeterinarioCreate, VeterinarioList, VeterinarioUpdate, VeterinarioDetail, VeterinarioDelete, AdminCreate, AdminDelete, AdminDetail, AdminList, AdminUpdate

urlpatterns = [
    path('agregar_propietario', PropietarioCreate.as_view(), name='propietario_form'),
    path('listar_propietario', PropietarioList.as_view(), name='propietario_listar'),
    path('eliminar_propietario/<pk>', PropietarioDelete.as_view(), name='propietario_eliminar'),
    path('detalles_propietario/<pk>', PropietarioDetail.as_view(), name='propietario_detalles'),
    path('actualizar_propietario/<pk>', PropietarioUpdate.as_view(), name='propietario_actualizar'),

    path('agregar_veterinario', VeterinarioCreate.as_view(), name='veterinario_form'),
    path('listar_veterinario', VeterinarioList.as_view(), name='veterinario_listar'),
    path('detalles_veterinario/<pk>', VeterinarioDetail.as_view(), name='veterinario_detalles'),
    path('eliminar_veterinario/<pk>', VeterinarioDelete.as_view(), name='veterinario_eliminar'),
    path('actualizar_veterinario/<pk>', VeterinarioUpdate.as_view(), name='veterinario_actualizar'),

    path('agregar_admin', AdminCreate.as_view(), name='admin_form'),
    path('listar_admin', AdminList.as_view(), name='admin_listar'),
    path('detalles_admin/<pk>', AdminDetail.as_view(), name='admin_detalles'),
    path('eliminar_admin/<pk>', AdminDelete.as_view(), name='admin_eliminar'),
    path('actualizar_admin/<pk>', AdminUpdate.as_view(), name='admin_actualizar'),
]