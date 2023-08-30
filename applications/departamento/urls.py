""" Imports """
from django.urls import path
from . import views



""" Name """
app_name = 'departamento_app'



""" Pattern """
urlpatterns = [
    path('list-department/', views.DepartamentoListView.as_view(), name='list_department'),
    path('new-department/', views.NewDepartmentView.as_view(), name='new_department')
]






