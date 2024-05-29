from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaForm
from .models import Alumno, Curso, Nota
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
 