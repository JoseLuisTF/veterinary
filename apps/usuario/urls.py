from django.urls import path
from apps.usuario.views import PropietarioCreate,PropietarioList,PropietarioDelete,PropietarioUpdate,PropietarioDetail, VeterinarioCreate, VeterinarioList

urlpatterns = [
    path('Agregar_Propietario', (PropietarioCreate.as_view()), name='propietario_form'),
    path('Listar_Propietario', PropietarioList.as_view(), name='propietario_listar'),
    path('Eliminar_Propietario/<pk>', PropietarioDelete.as_view(), name='propietario_eliminar'),
    path('Detalles_Propietario/<pk>', PropietarioDetail.as_view(), name='propietario_detalles'),
    path('Actualizar_Propietario/<pk>', PropietarioUpdate.as_view(), name='propietario_actualizar'),

    path('Agregar_Veterinario', VeterinarioCreate.as_view(), name='veterinario_form'),
    path('Listar_Veterinario', VeterinarioList.as_view(), name='veterinario_listar'),
]