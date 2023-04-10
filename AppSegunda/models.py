from django.db import models

# Create your models here.
class reserva(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrada= models.DateField()
    pagado= models.BooleanField()