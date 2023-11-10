# Generated by Django 4.2 on 2023-11-09 04:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_titulo_enriquecido_alter_post_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='titulo_enriquecido',
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]