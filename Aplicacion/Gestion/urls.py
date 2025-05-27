from django.urls import path
from . import views

urlpatterns = [
    # Rutas para PROFESOR
    path('', views.profesor),
    path('profesor/', views.profesor, name='profesor'),
    path('nuevoProfesor/', views.nuevoProfesor, name='nuevoProfesor'),
    path('guardarProfesor/', views.guardarProfesor, name='guardarProfesor'),
    path('editarProfesor/<cedula>/', views.editarProfesor, name='editarProfesor'),
    path('procesarEdicionProfesor/<cedula>/', views.procesarEdicionProfesor, name='procesarEdicionProfesor'),
    path('eliminarProfesor/<cedula>/', views.eliminarProfesor, name='eliminarProfesor'),

    # Rutas para MATERIA
    path('materia/', views.materia, name='materia'),
    path('nuevaMateria/', views.nuevaMateria, name='nuevaMateria'),
    path('guardarMateria/', views.guardarMateria, name='guardarMateria'),
    path('editarMateria/<int:id>/', views.editarMateria, name='editarMateria'),
    path('procesarEdicionMateria/<int:id>/', views.procesarEdicionMateria, name='procesarEdicionMateria'),
    path('eliminarMateria/<int:id>/', views.eliminarMateria, name='eliminarMateria'),

    # Rutas para ESTUDIANTE
    path('estudiante/', views.estudiante, name='estudiante'),
    path('nuevoEstudiante/', views.nuevoEstudiante, name='nuevoEstudiante'),
    path('guardarEstudiante/', views.guardarEstudiante, name='guardarEstudiante'),
    path('editarEstudiante/<cedula>/', views.editarEstudiante, name='editarEstudiante'),
    path('procesarEdicionEstudiante/<cedula>/', views.procesarEdicionEstudiante, name='procesarEdicionEstudiante'),
    path('eliminarEstudiante/<cedula>/', views.eliminarEstudiante, name='eliminarEstudiante'),

    # Rutas para MATRICULA
    path('matricula/', views.matricula, name='matricula'),
    path('nuevaMatricula/', views.nuevaMatricula, name='nuevaMatricula'),
    path('guardarMatricula/', views.guardarMatricula, name='guardarMatricula'),
    path('editarMatricula/<int:id>/', views.editarMatricula, name='editarMatricula'),
    path('procesarEdicionMatricula/<int:id>/', views.procesarEdicionMatricula, name='procesarEdicionMatricula'),
    path('eliminarMatricula/<int:id>/', views.eliminarMatricula, name='eliminarMatricula'),
]
