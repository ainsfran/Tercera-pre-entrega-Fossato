from django.urls import path
from AppCoder import views

urlpatterns = [
    path ("",views.InicioView, name='Inicio'),
    path ("hospedaje", views.HospedajeView, name='Hospedaje'),
    path ("huesped", views.HuespedView,name='Huesped'),
    path ("reserva", views.ReservaView, name='Reserva'),
    path ("busquedaHospedaje", views.busquedaHospedajeView, name="BusquedaHospedaje"),
    path ("buscar/", views.buscar),
    path ('hospedajeFormulario', views.HospedajeFormulario, name="hospedajeFormulario"),
    path ('huespedFormulario', views.HuespedFormulario, name="huespedFormulario"),
    path ('reservaFormulario', views.ReservaFormulario, name="reservaFormulario"),

    
]