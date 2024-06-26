from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaForm
from .models import Alumno, Curso, NotaAlumnosPorCurso
# Create your views here.

def crearAlumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaAlumnos')
    else:
        form = AlumnoForm()
    return render(request, 'gestion/crearAlumno.html', {'form': form}) 

def listaAlumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestion/listaAlumnos.html', {'alumnos': alumnos})

def crearCurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaCursos')
    else:
        form = CursoForm()
    return render(request, 'gestion/crearCurso.html', {'form': form})

def listaCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion/listaCursos.html', {'cursos': cursos})

def crearNota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaNotas')
    else:
        form = NotaForm()
    return render(request, 'gestion/crearNota.html', {'form': form})

def listaNotas(request):
    notas = NotaAlumnosPorCurso.objects.all()
    return render(request, 'gestion/listaNotas.html', {'notas': notas})
