from django.db import models
from apps.mascota.models import Mascota
from apps.usuario.models import Profile


# Create your models here.


class Fecha(models.Model):
    id_fecha = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=12, unique=True)
    date = models.DateField()

    def __str__(self):
        return '{}'.format(self.dia) + ' - ' + '{}'.format(self.date)


class HoraGeneral(models.Model):
    id_hora_general = models.AutoField(primary_key=True)
    date = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    time = models.TimeField()
    ocupado = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.time)


class CitaGeneral(models.Model):
    id_cita_general = models.AutoField(primary_key=True)
    tipo_cita = models.CharField(max_length=20)
    date = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    time = models.OneToOneField(HoraGeneral, on_delete=models.CASCADE, limit_choices_to={'ocupado': False})
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    informacion = models.TextField(max_length=100, blank=True, null=True)


class CitaEstetica(models.Model):
    id_cita_estetica = models.AutoField(primary_key=True)
    tipo_cita = models.CharField(max_length=20)
    date = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    time = models.OneToOneField(HoraGeneral, on_delete=models.CASCADE, limit_choices_to={'ocupado': False})
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    baño = models.BooleanField()
    corte = models.BooleanField()
    unias = models.BooleanField()
    recoger = models.BooleanField()
    informacion = models.TextField(max_length=100, blank=True, null=True)


class Guarderia(models.Model):
    id_guarderia = models.AutoField(primary_key=True)
    tipo_cita = models.CharField(max_length=20)
    date_inicio = models.DateField()
    date_fin = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    recoger = models.BooleanField()
    informacion = models.TextField(max_length=100, blank=True, null=True)
