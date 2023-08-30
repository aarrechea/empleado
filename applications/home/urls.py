""" Imports """
from django.urls import path
from . import views



""" name """
app_name = "home_app"



""" Patterns """
urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add_home/', views.PruebaCreateView.as_view(), name="add_home"),
    path('resume-foundation/', views.ResumeFoundationView.as_view(), name="resume"),
]






