""" Imports """
from django import forms



""" Create department """
class NewDepartmentForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)


