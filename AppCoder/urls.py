from django.urls import path
from AppCoder import views

#app_name='AppCoder'

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
    #path ("leerHospedaje", views.leerHospedaje, name="LeerHospedaje"),
    #path('eliminarHospedaje/<hospedaje_nombre>',views.eliminarHospedaje, name="eliminarHospedaje"),
    #path('editarHospedaje/<hospedaje_nombre>', views.editarHospedaje,name='EditarHospedaje'),
    path('hospedaje/list',views.HospedajeList.as_view(), name='List'),
    path('<int:pk>', views.HospedajeDetalle.as_view(), name='Detail'),
    path('nuevo/<int:pk>', views.HospedajeCreacion.as_view(), name='New'),
    path('editar/<int:pk>', views.HospedajeUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.HospedajeDelete.as_view(), name='Delete'),



]