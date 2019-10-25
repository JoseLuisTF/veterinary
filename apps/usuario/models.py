from django.db import models


# Create your models here.

class Propietario(models.Model):
    id_propietario = models.AutoField(max_length=5, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cc = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    edad = models.IntegerField()
    SEXOS = (
            ('H', 'Hombre'),
            ('M', 'Mujer'),
    )

    sexo = models.CharField(max_length=15, choices=SEXOS)
    celular = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombres+' '+self.apellidos


class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario

class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cc = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    edad = models.IntegerField()
    SEXOS = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    sexo = models.CharField(max_length=15, choices=SEXOS)
    celular = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return '{}'.format(self.nombres, self.apellidos)