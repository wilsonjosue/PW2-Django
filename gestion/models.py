from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    matricula = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}."
    
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Nota(models.Model): 
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        
        return f"{self.alumno} - {self.curso}: {self.nota}"
   

