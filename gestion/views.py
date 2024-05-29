from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaForm
from .models import Alumno, Curso, Nota
# Create your views here.

def crearAlumno():
