from django.db import models

# Create your models here.
class hospedaje(models.Model):
    
    nombre=models.CharField(max_length=40)
    HabDispo=models.IntegerField()

class huesped(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class reserva(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrada= models.DateField()
    pagado= models.BooleanField()

