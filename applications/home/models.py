""" Imports """
from django.db import models



""" Prueba model """
class Prueba(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    cantidad = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.titulo} - {self.subtitulo}"

