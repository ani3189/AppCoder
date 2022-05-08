from re import template
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('cursos', views.cursos, name = "Cursos"),
    path('profesores', views.profesores, name = "Profesores"),
    path('estudiantes', views.estudiantes, name = "Estudiantes"),
    path('entregables', views.enrtegables, name = "Entregables"),
    path('busqueda/', views.busqueda, name="busqueda"),
    path('buscar/', views.buscar),
    path('listaProfes/', views.listaProfesores, name='ListaProfesores'),
    path("chauProfe/<profesor_nombre>", views.borrarProfesores, name="EliminarProfesor"),
    path("editarProfe/<profesor_nombre>", views.editarProfesores, name="EditarProfesor"),
    path("curso/lista", views.CursoList.as_view(), name='ListaCursos'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout')
]