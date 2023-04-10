from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class reservaFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    fechaDeEntrada= forms.DateField()
    pagado= forms.BooleanField()

