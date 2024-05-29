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

class Nota 

   

