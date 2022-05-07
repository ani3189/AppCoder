from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):

    if request.method == 'POST':

        miFormulario = CursoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    
    else:
        miFormulario = CursoForm()
    
    return render(request,"AppCoder/cursos.html", {"miFormulario":miFormulario})

def profesores(request):
    if request.method == 'POST':
        miFormulario3 = ProfesorForm(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid():
            info = miFormulario3.cleaned_data
            profesor = Profesor(
                nombre = info['nombre'],
                apellido = info['apellido'],
                mail = info['mail'],
                profesion = info['profesion'],
            )
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario3 = ProfesorForm()

    return render(request, "AppCoder/profesores.html", {"miFormulario3":miFormulario3})
    
def estudiantes(request):
    
    if request.method == 'POST':

        miFormulario2 = EstudianteForm(request.POST)

        print(miFormulario2)

        if miFormulario2.is_valid():
            informacion = miFormulario2.cleaned_data
            estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")
    
    else:
        miFormulario2 = EstudianteForm()
    
    return render(request,"AppCoder/estudiantes.html", {"miFormulario2":miFormulario2})

def enrtegables(request):
    return render(request, "AppCoder/entregables.html")

def busqueda(request):
    return render(request, "AppCoder/busqueda.html")

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/buscar.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)

