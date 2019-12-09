from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    telephone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile_detalles', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


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
