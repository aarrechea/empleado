""" Imports """
from django.urls import path
from . import views



""" Application name """
app_name = 'persona_app'


""" Patterns """
urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('list-all/', views.ListAllEmployees.as_view(), name='list_all'),
    path('list-by-department/<str:department>/', views.ListEmployeesByDepartment.as_view(), name='list_by_department'),
    path('list-by-key/', views.ListByKeyWord.as_view()),
    path('list-habilidades/', views.HabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add/', views.EmployeeCreateView.as_view(), name='add_empleado'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('update/<pk>/', views.EmpleadoUpdate.as_view(), name='update'),
    path('delete/<pk>/', views.EmpleadoDeleteView.as_view(), name='delete'),
    path('lista-admin/', views.ListEmployeesAdmin.as_view(), name='lista_empleados_admin'),
]






