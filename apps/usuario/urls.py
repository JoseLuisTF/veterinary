from django.urls import path, re_path
from apps.usuario.views import ProfileDetail, ProfileUpdate

urlpatterns = [
    # path('listar', PropietarioList.as_view(), name='propietario_listar'),
    # path('eliminar/<pk>', PropietarioDelete.as_view(), name='propietario_eliminar'),
    path('detalles/<pk>', ProfileDetail.as_view(), name='profile_detalles'),
    path('actualizar/<pk>', ProfileUpdate.as_view(), name='profile_actualizar'),

    # path('agregar_veterinario', VeterinarioCreate.as_view(), name='veterinario_form'),
    # path('listar_veterinario', VeterinarioList.as_view(), name='veterinario_listar'),
    # path('detalles_veterinario/<pk>', VeterinarioDetail.as_view(), name='veterinario_detalles'),
    # path('eliminar_veterinario/<pk>', VeterinarioDelete.as_view(), name='veterinario_eliminar'),
    # path('actualizar_veterinario/<pk>', VeterinarioUpdate.as_view(), name='veterinario_actualizar'),

]
