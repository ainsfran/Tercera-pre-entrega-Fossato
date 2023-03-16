from django.shortcuts import render
from AppCoder.models import hospedaje, huesped, reserva
from django.http import HttpResponse
from AppCoder.forms import hospedajeFormulario
from AppCoder.forms import huespedFormulario
from AppCoder.forms import reservaFormulario


# Create your views here

def InicioView (request):
    return render(request, "inicio.html")

def HospedajeView(request): 
 return render(request,"hospedaje.html")

def HuespedView (request):
    return render(request,"huesped.html")

def ReservaView (request):
    return render(request,"reserva.html")

def busquedaHospedajeView(request):
   return render(request, "busquedaHospedaje.html")

def resultadoBusquedaView(request):
   return render(request, "resultadosBusqueda.html")

def HospedajeFormulario (request):
    form = hospedajeFormulario(request.POST or None)
    if request.method == "POST" and form.is_valid():
        informacion= form.cleaned_data
        Hospedaje = hospedaje(nombre=informacion['nombre'], HabDispo=informacion['habDispo'])
        Hospedaje.save()
        return render(request, 'inicio.html')

    else:
       miFormulario= hospedajeFormulario()

    
    return render(request, "hospedajeFormulario.html", {'miFormulario': miFormulario})

def HuespedFormulario (request):
    form = huespedFormulario(request.POST or None)
    if request.method == "POST" and form.is_valid():
        informacion= form.cleaned_data
        Huesped = huesped(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
        Huesped.save()
        return render(request, 'inicio.html')

    else:
       miFormulario= huespedFormulario()

    
    return render(request, "huespedFormulario.html", {'miFormulario': miFormulario})

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


#BUSQUEDA

def buscar(request):
   if request.GET["nombre"]:
      nombre= request.GET["nombre"]
      hospedajesMatch = hospedaje.objects.filter(nombre__icontains=nombre)  

      if hospedajesMatch.exists():

         for x in hospedajesMatch:
            print(x.nombre)
            print(x.HabDispo)

         return render(request,"resultadosBusqueda.html", {"nombre":nombre, "hospedajes": hospedajesMatch})

      return render(request,"resultadosBusqueda.html", {"nombre":nombre, "hospedajes": None})

   else:
      respuesta= "no enviaste datos."
    
   return HttpResponse(respuesta)