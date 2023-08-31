# Generated by Django 4.2.4 on 2023-08-17 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_alter_departamento_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Mis Departamentos'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]
