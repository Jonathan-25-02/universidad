from django.db import models

# Create your models here.
# Modelo de Profesor
class Profesor(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"

# Modelo de Materia
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - Prof: {self.profesor.nombre}"

# Modelo de Estudiante
class Estudiante(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()


    def __str__(self):
        return f"{self.nombre} ({self.cedula})"

# Modelo de Matricula
class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.materia.nombre} ({self.fecha_matricula})"
