from django.db import models

# Define los modelos de la aplicación

# Modelo para representar a un empleado
class Empleado(models.Model):
    # Campo para el nombre real del empleado
    nombre_real = models.CharField(max_length=100)
    # Campo para el apodo o nickname del empleado
    nickname = models.CharField(max_length=100)
    # Campo para la nube o cloudad del empleado
    cloudad = models.CharField(max_length=100)
    # Campo para el correo electrónico del empleado
    correo = models.CharField(max_length=100)
    # Campo para almacenar la relación con el grupo al que pertenece el empleado
    grupo = models.ForeignKey('Grupo', on_delete=models.SET_NULL, null=True)

    # Método para representar el objeto empleado como una cadena de texto
    def __str__(self):
        return self.nombre_real

# Modelo para representar un grupo
class Grupo(models.Model):
    # Campo para el nombre del grupo
    nombre = models.CharField(max_length=100)

    # Método para representar el objeto grupo como una cadena de texto
    def __str__(self):
        return self.nombre
