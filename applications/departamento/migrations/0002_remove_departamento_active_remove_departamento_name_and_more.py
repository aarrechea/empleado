# Generated by Django 4.2.4 on 2023-08-16 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='Active',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='Short name',
        ),
        migrations.AddField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(default='None', max_length=20, verbose_name='Short name'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='name',
            field=models.CharField(default='None', max_length=50, verbose_name='Name'),
        ),
    ]
