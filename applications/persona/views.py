""" Imports """
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm


""" Home page """
class InicioView(TemplateView):
    template_name = 'inicio.html'


""" List employees """
class ListAllEmployees(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')        
        lista = Empleado.objects.filter(full_name__icontains=palabra_clave)
                 
        return lista
    
        
""" Admin List """
class ListEmployeesAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    
        
""" List employees by department """
class ListEmployeesByDepartment(ListView):
    template_name = 'persona/list_by_department.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        department = self.kwargs['department']        
        lista = Empleado.objects.filter(departamento__name = department) 
        
        return lista


""" List by key word """
class ListByKeyWord(ListView):
    template_name = 'persona/list_by_key_word.html'
    context_object_name = 'empleados'
        
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword')
        lista = Empleado.objects.filter(departamento__name=palabra_clave) 
                 
        return lista
            
    
""" Listar habilidades """
class HabilidadesEmpleado(ListView):
    template_name = 'persona/list_habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
                
        return empleado.habilidades.all() 
    
        
""" Detail view employee """
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/emp_detail_view.html"
    context_object_name = 'employee'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Título'
        return context
    
        
""" Success view """    
class SuccessView(TemplateView):
    template_name = 'persona/success.html'
    

""" Create employee """    
class EmployeeCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    # fields = ('__all__')
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar']
    form_class = EmpleadoForm
    
    success_url = reverse_lazy('persona_app:list_all')
    #success_url = '.' # same url
    
    def form_valid(self, form):
        empleado = form.save(commit=False) # assigning to empleado's variable without saving
        empleado.full_name = f"{empleado.first_name} {empleado.last_name}"
        empleado.save()
        
        return super(EmployeeCreateView, self).form_valid(form)
    

""" Update """
class EmpleadoUpdate(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado    
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:list_all')
    
    # Before valid method
    def post(self, request: HttpRequest, *args: str, **kwargs: Any):        
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):                
        return super(EmpleadoUpdate, self).form_valid(form)
        
    
""" Delete view """
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy("persona_app:list_all")
    
    
    