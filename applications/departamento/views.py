""" Imports """
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from applications.persona.models import Empleado
from .forms import NewDepartmentForm
from .models import Departamento



""" New department """
class NewDepartmentView(FormView):
    template_name = "departamento/new_department.html"
    form_class = NewDepartmentForm
    success_url = '/'
    
    def form_valid(self, form): # self is the context
        depto = Departamento(
            name = form.cleaned_data['department'],
            short_name = form.cleaned_data['short_name']
        )
        depto.save()
        
        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']                        
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job=1,
            departamento = depto,
        )
        
        return super(NewDepartmentView, self).form_valid(form)
    


""" List department """    
class DepartamentoListView(ListView):
    template_name = 'departamento/list.html'
    model = Departamento
    context_object_name = 'departamentos'
    
    
    