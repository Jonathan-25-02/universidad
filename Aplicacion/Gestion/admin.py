from django.contrib import admin

from .models import Profesor,   Materia, Estudiante, Matricula 
# Register your models here.
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Estudiante)
admin.site.register(Matricula)