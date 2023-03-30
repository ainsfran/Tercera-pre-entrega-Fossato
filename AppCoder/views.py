from django.shortcuts import render
from AppCoder.models import hospedaje, huesped, reserva
from django.http import HttpResponse
from AppCoder.forms import hospedajeFormulario
from AppCoder.forms import huespedFormulario
from AppCoder.forms import reservaFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppCoder.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#class ClaseQueNecesitaLogin(LoginRequiredMixin):
@login_required
def InicioView(request):
   return render(request, "inicio.html")



def login_request(request):
   if request.method == "POST":
      form= AuthenticationForm(request, data= request.POST)
      if form.is_valid():
         usuario= form.cleaned_data.get("username")
         contras= form.cleaned_data.get("password")

         user= authenticate(username= usuario, password= contras)
         if user is not None:
            login(request,user)
            return render(request,"inicio.html",{"mensaje":f"Bienvenido/a {usuario}"})
         else:
            return render(request,"inicio.html",{"mensaje":f"Error, datos incorrectos"})
      else:
         return render(request,"inicio.html",{"mensaje":"Error, formulario erroneo"}) 
   form= AuthenticationForm()
   return render(request,"login.html",{"form":form})



            



#def InicioView (request):
 #   return render(request, "inicio.html")

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

#CRUD leer


"""def leerHospedaje(request):
   Hospedaje=hospedaje.objects.all()
   contexto = {"hospedaje":Hospedaje}
   return render (request,"leerHospedaje.html",contexto)

def eliminarHospedaje(request,hospedaje_nombre):
   Hospedaje= hospedaje.objects.get(nombre=hospedaje_nombre)
   Hospedaje.delete()
   Hospedaje_1= hospedaje.objects.all()
   contexto= {"Hospedajes": Hospedaje_1}
   return render(request,"leerHospedaje.html",contexto)

def editarHospedaje(request, hospedaje_nombre):
   Hospedaje= hospedaje.objects.get(nombre=hospedaje_nombre)
   if request.method == 'POST':
      miFormulario= hospedajeFormulario(request.POST)
      print(miFormulario)
      if miFormulario.is_valid:
         informacion=miFormulario.cleaned_data
         Hospedaje.nombre= informacion['nombre']
         Hospedaje.HabDispo=informacion['HabDispo']

         Hospedaje.save()
         return render(request,"inicio.html")
      
   else:
      miFormilario= hospedajeFormulario(initial={'nombre': Hospedaje.nombre,'HabDispo': Hospedaje.HabDispo })
      return render(request,'editarHospedaje.html',{'miFormulario':miFormilario, "hospedaje_nombre":hospedaje_nombre} )
"""

class HospedajeList(ListView):
   
   model= hospedaje
   template_mame="AppCoder/hospedaje_list.html"

class HospedajeDetalle(DetailView):
   model= hospedaje
   template_name="AppCoder/hospedaje_detalle.html"

class HospedajeCreacion(CreateView):
   model= hospedaje
   template_name="AppCoder/hospedaje_form.html"
   success_url=reverse_lazy("hospedaje/list")
   fields= ['nombre','HabDispo']

class HospedajeUpdate(DeleteView):
   model= hospedaje
   success_url="hospedaje/list"
   template_name="AppCoder/hospedaje_form.html"
   fields= ['nombre','HabDispo']

class HospedajeDelete(DeleteView):
   model= hospedaje
   template_name="AppCoder/hospedaje_confirm_delete.html"
   success_url="hospedaje/list"

 #registro

def register(request):
   if request.method =="POST":
      #form = UserCreationForm(request.POST)
      form= UserRegisterForm(request.POST)
      if form.is_valid():
         username= form.cleaned_data["username"]
         form.save()
         return render(request,"inicio.html", {"mensaje":"Usuario Creado "})
   else:
      #form = UserCreationForm()
      form= UserRegisterForm()

   return render(request,"registro.html",{"form":form})
