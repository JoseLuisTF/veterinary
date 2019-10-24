# Generated by Django 2.2.6 on 2019-10-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id_propietario', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('cc', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('emailufps', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id_veterinario', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('cc', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
