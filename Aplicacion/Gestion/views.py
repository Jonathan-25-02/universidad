from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profesor, Materia, Estudiante, Matricula

# PROFESORES

def profesor(request):
    lista = Profesor.objects.all()
    return render(request, "profesor.html", {'profesores': lista})

def nuevoProfesor(request):
    return render(request, "nuevoProfesor.html")

def guardarProfesor(request):
    Profesor.objects.create(
        cedula=request.POST["cedula"],
        nombre=request.POST["nombre"],
        correo=request.POST["correo"],
        logo=request.FILES.get("logo")
    )
    messages.success(request, "Profesor guardado exitosamente")
    return redirect('/profesor')

def editarProfesor(request, cedula):
    prof = Profesor.objects.get(cedula=cedula)
    return render(request, "editarProfesor.html", {'profesorEditar': prof})

def procesarEdicionProfesor(request, cedula):
    prof = Profesor.objects.get(cedula=cedula)
    prof.nombre = request.POST["nombre"]
    prof.correo = request.POST["correo"]
    prof.logo=request.FILES.get("logo")
    prof.save()
    messages.success(request, "Profesor actualizado exitosamente")
    return redirect('/profesor')

def eliminarProfesor(request, cedula):
    Profesor.objects.get(cedula=cedula).delete()
    return redirect('/profesor')


# MATERIAS

def materia(request):
    lista = Materia.objects.all()
    return render(request, "materia.html", {'materias': lista})

def nuevaMateria(request):
    profesores = Profesor.objects.all()
    return render(request, "nuevaMateria.html", {'profesores': profesores})

def guardarMateria(request):
    profesor = Profesor.objects.get(cedula=request.POST["profesor"])
    Materia.objects.create(
        codigo=request.POST["codigo"],
        nombre=request.POST["nombre"],
        logo=request.FILES.get("logo"),
        profesor=profesor
        
    )
    messages.success(request, "Materia guardada exitosamente")
    return redirect('/materia')

def editarMateria(request, id):
    mat = Materia.objects.get(id_materia=id)
    profesores = Profesor.objects.all()
    return render(request, "editarMateria.html", {'materiaEditar': mat, 'profesores': profesores})

def procesarEdicionMateria(request, id):
    mat = Materia.objects.get(id_materia=id)
    mat.codigo = request.POST["codigo"]  # <- Esto es lo que te faltaba, mi cielo
    mat.nombre = request.POST["nombre"]
    mat.profesor = Profesor.objects.get(cedula=request.POST["profesor"])
    mat.logo=request.FILES.get("logo")
    mat.save()
    messages.success(request, "Materia actualizada exitosamente")
    return redirect('/materia')

def eliminarMateria(request, id):
    Materia.objects.get(id_materia=id).delete()
    return redirect('/materia')


# ESTUDIANTES

def estudiante(request):
    lista = Estudiante.objects.all()
    return render(request, "estudiante.html", {'estudiantes': lista})

def nuevoEstudiante(request):
    return render(request, "nuevoEstudiante.html")

def guardarEstudiante(request):
    Estudiante.objects.create(
        cedula=request.POST["cedula"],
        nombre=request.POST["nombre"],
        correo=request.POST["correo"],
        logo=request.FILES.get("logo")
    )
    messages.success(request, "Estudiante guardado exitosamente")
    return redirect('/estudiante')

def editarEstudiante(request, cedula):
    est = Estudiante.objects.get(cedula=cedula)
    return render(request, "editarEstudiante.html", {'estudianteEditar': est})

def procesarEdicionEstudiante(request, cedula):
    est = Estudiante.objects.get(cedula=cedula)
    est.nombre = request.POST["nombre"]
    est.correo = request.POST["correo"]
    est.logo=request.FILES.get("logo")

    est.save()
    messages.success(request, "Estudiante actualizado exitosamente")
    return redirect('/estudiante')

def eliminarEstudiante(request, cedula):
    Estudiante.objects.get(cedula=cedula).delete()
    return redirect('/estudiante')


# MATRICULAS

def matricula(request):
    lista = Matricula.objects.all()
    return render(request, "matricula.html", {'matriculas': lista})

def nuevaMatricula(request):
    estudiantes = Estudiante.objects.all()
    materias = Materia.objects.all()
    return render(request, "nuevaMatricula.html", {'estudiantes': estudiantes, 'materias': materias})

def guardarMatricula(request):
    estudiante = Estudiante.objects.get(cedula=request.POST["estudiante"])
    materia = Materia.objects.get(id_materia=request.POST["materia"])
    ciclo = request.POST["ciclo"]
    logo=request.FILES.get("logo")

    Matricula.objects.create(
        estudiante=estudiante,
        materia=materia,
        ciclo=ciclo,
        logo=logo
    )

    messages.success(request, "Matrícula guardada exitosamente")
    return redirect('/matricula')

def editarMatricula(request, id):
    
    mat = Matricula.objects.get(id_matricula=id)
    estudiantes = Estudiante.objects.all()
    materias = Materia.objects.all()
    
    return render(request, "editarMatricula.html", {
        'matriculaEditar': mat,
        'estudiantes': estudiantes,
        'materias': materias,
        
    })

def procesarEdicionMatricula(request, id):
    mat = Matricula.objects.get(id_matricula=id)
    mat.estudiante = Estudiante.objects.get(cedula=request.POST["estudiante"])
    mat.materia = Materia.objects.get(id_materia=request.POST["materia"])
    mat.ciclo = request.POST["ciclo"]
    mat.logo=request.FILES.get("logo")
    mat.save()

    messages.success(request, "Matrícula actualizada exitosamente")
    return redirect('/matricula')

def eliminarMatricula(request, id):
    Matricula.objects.get(id_matricula=id).delete()
    return redirect('/matricula')
