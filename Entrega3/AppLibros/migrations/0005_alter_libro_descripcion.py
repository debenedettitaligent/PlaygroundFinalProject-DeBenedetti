# Generated by Django 4.2.7 on 2023-12-12 23:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppLibros', '0004_alter_libro_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
