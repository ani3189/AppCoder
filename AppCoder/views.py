from multiprocessing import AuthenticationError
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
            if user:
                login(request,user)
                return render (request, "AppCoder/inicio.html", {'mensaje':f"Bienvenido {user}"})
        else:
            return render (request, "AppCoder/inicio.html", {'mensaje':"Error, datos incorrectos"})
    else:
        form = AuthenticationForm()

    return render (request, "AppCoder/login.html", {'form':form})

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

@login_required
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


def listaProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

def borrarProfesores(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto={"profesores":profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesores(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.mail = informacion['mail']
            profesor.profesion = informacion['profesion']

            profesor.save() 

            return render (request, "AppCoder/inicio.html")
    else:
        miFormulario= ProfesorForm(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido,
        'mail':profesor.mail, 'profesion':profesor.profesion})
    return render(request, "AppCoder/editarProfesor.html", {'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})

class CursoList (LoginRequiredMixin,ListView):
    model = Curso
    template_name = "AppCoder/listacursos.html"

class CursoDetalle (DeleteView):
    model = Curso
    template_name = "AppCoder/cursoDetalle.html"

class CursoCreacion (CreateView):
    model = Curso
    success_url = "/AppCoder/curso/lista"
    fields = ['nombre', 'camada']

class CursoUpdate (UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/lista"
    fields = ['nombre', 'camada']

class CursoDelete (DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/lista"
    