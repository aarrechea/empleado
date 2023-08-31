""" Imports """
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm



""" Index View """
class IndexView(TemplateView):
    template_name = "home/home.html"
    
class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"    
        


""" List view """    
class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['A', 'B', 'C']
    context_object_name = "lista_prueba"
    
    

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = "lista_prueba"
    
    
    
""" Create view """    
class PruebaCreateView(CreateView):
    template_name = "home/add_home.html"
    model = Prueba
    form_class = PruebaForm
    success_url = "/" # go to main page
    




