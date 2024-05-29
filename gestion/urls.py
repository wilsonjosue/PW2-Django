from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/crear/', views.crearAlumno, name='crearAlumno'),
    path('alumnos/', views.listaAlumnos, name='listaAlumnos'),
    path('cursos/crear/', views.crearCurso, name='crearCurso'),
    path('cursos/', views.listaCursos, name='listaCursos'),
    path('notas/crear/', views.crearNota, name='crearNota'),
    path('notas/', views.listaNotas, name='listaNotas'),
]