from django.db import models

# Create your models here.
class curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrega= models.DateField()
    entregado= models.BooleanField()

    