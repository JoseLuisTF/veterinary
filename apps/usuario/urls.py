from django.urls import path
from apps.usuario.views import PropietarioCreate, PropietarioList, PropietarioDelete, PropietarioUpdate, PropietarioDetail, \
    VeterinarioCreate, VeterinarioList, VeterinarioUpdate, VeterinarioDetail, VeterinarioDelete, AdminCreate, AdminDelete, AdminDetail, AdminList, AdminUpdate

urlpatterns = [
    path('Agregar_Propietario', PropietarioCreate.as_view(), name='propietario_form'),
    path('Listar_Propietario', PropietarioList.as_view(), name='propietario_listar'),
    path('Eliminar_Propietario/<pk>', PropietarioDelete.as_view(), name='propietario_eliminar'),
    path('Detalles_Propietario/<pk>', PropietarioDetail.as_view(), name='propietario_detalles'),
    path('Actualizar_Propietario/<pk>', PropietarioUpdate.as_view(), name='propietario_actualizar'),

    path('Agregar_Veterinario', VeterinarioCreate.as_view(), name='veterinario_form'),
    path('Listar_Veterinario', VeterinarioList.as_view(), name='veterinario_listar'),
    path('Detalles_Veterinario/<pk>', VeterinarioDetail.as_view(), name='veterinario_detalles'),
    path('Eliminar_Veterinario/<pk>', VeterinarioDelete.as_view(), name='veterinario_eliminar'),
    path('Actualizar_Veterinario/<pk>', VeterinarioUpdate.as_view(), name='veterinario_actualizar'),

    path('Agregar_Admin', AdminCreate.as_view(), name='admin_form'),
    path('Listar_Admin', AdminList.as_view(), name='admin_listar'),
    path('Detalles_Admin/<pk>', AdminDetail.as_view(), name='admin_detalles'),
    path('Eliminar_Admin/<pk>', AdminDelete.as_view(), name='admin_eliminar'),
    path('Actualizar_Admin/<pk>', AdminUpdate.as_view(), name='admin_actualizar'),
]