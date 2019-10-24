from django.db import models
from apps.usuario.models import Propietario

# Create your models here.


class Especie(models.Model):
    id_especie = models.AutoField(primary_key=True)
    nom_especie = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.nom_especie)


class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nom_raza = models.CharField(max_length=15)
    especie = models.ForeignKey(Especie, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nom_raza)


class Mascota(models.Model):
    id_raza = models.AutoField(primary_key=True)
    alias = models.CharField(max_length=15)
    especie = models.ForeignKey(Especie, null=True, blank=True, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, null=True, blank=True, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=15)
    edad = models.IntegerField()
    propietario = models.OneToManyField(Propietario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.alias)
