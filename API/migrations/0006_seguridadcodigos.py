# Generated by Django 5.1.2 on 2024-10-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_rename_contrasena_usuario_codigoseguridad'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeguridadCodigos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Correo', models.CharField(max_length=50)),
                ('CodigoSeguridad', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
            ],
        ),
    ]