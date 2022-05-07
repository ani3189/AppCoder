from django import forms

class CursoForm(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
    profesion = forms.CharField()

class EntregableForm(forms.Form):
    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()
