# Generated by Django 4.2 on 2023-11-09 04:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_categoria_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titulo_enriquecido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
