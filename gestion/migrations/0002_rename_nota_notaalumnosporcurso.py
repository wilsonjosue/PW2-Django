# Generated by Django 5.0.6 on 2024-05-29 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nota',
            new_name='NotaAlumnosPorCurso',
        ),
    ]