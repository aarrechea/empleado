""" Imports """
from django import forms
from .models import Prueba



""" Prueba form """
class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder':'Enter title'
                }
            )
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a diez')
        
        return cantidad




