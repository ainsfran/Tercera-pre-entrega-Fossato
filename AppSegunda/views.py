from django.shortcuts import render
from AppSegunda.models import reserva #Avatar
from django.http import HttpResponse
#from AppSegunda.forms import  AvatarFormulario
from AppSegunda.forms import reservaFormulario

# Create your views here.
def ReservaView (request):
    return render(request,"reserva.html")

def ReservaFormulario (request):
    
    form = reservaFormulario(request.POST or None)
    if request.method == "POST" and form.is_valid():
        informacion= form.cleaned_data
        Reserva = reserva(nombre=informacion['nombre'], fecha=informacion['fecha'], pagado=informacion['pagado'])
        Reserva.save()
        return render(request, 'inicio.html')

    else:
       miFormulario= reservaFormulario()

    
    return render(request, "reservaFormulario.html", {'miFormulario': miFormulario})
