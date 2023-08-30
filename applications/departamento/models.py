""" Imports """
from django.db import models



""" Class Departamento """
class Departamento(models.Model):
    name = models.CharField('Name', max_length=50)
    short_name = models.CharField('Short name', max_length=20, unique=True)
    active = models.BooleanField("Active", default=True)
    
    
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Mis Departamentos'
        ordering = ['name']
        unique_together = ('name', 'short_name')
            

    def __str__(self):
        return f"{self.id} - {self.name}"
