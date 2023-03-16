from django import forms

class hospedajeFormulario(forms.Form):
    nombre= forms.CharField()
    habDispo= forms.IntegerField()

class huespedFormulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class reservaFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    fechaDeEntrada= forms.DateField()
    pagado= forms.BooleanField()
