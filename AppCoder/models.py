from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField(default=0)
    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.nombre, self.camada)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"
    def __str__(self):
        txt = "{0} , {1}"
        return txt.format(self.nombre, self.apellido)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    profesion = models.CharField(max_length=30)
    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
    def __str__(self):
        txt = "{0} , {1}"
        return txt.format(self.nombre, self.apellido)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    class Meta:
        verbose_name = "entregable"
        verbose_name_plural = "entregables"
    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)
