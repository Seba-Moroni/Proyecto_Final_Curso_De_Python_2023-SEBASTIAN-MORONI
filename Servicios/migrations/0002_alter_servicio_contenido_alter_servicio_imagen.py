# Generated by Django 4.2.5 on 2023-09-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]