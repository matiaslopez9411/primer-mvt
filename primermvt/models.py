from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    edad= models.IntegerField()
    dni= models.IntegerField()
    fecha_ingreso= models.DateFieldgi