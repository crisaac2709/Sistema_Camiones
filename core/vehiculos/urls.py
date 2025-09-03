from django.urls import path
from .views import RegistrarConductor, ActualizarConductor, ListarConductores, EliminarConductor, RegistrarVehiculo, ActualizarVehiculo, ListarVehiculos, EliminarVehiculo

app_name = "vehiculos"

urlpatterns = [
    # urls para conductores
    path('registrar_conductor/', RegistrarConductor, name="registrar_conductor"),
    path('actualizar_conductor/<int:pk>/', ActualizarConductor, name="actualizar_conductor"),
    path('listar_conductores/', ListarConductores, name="listar_conductores"),
    path('eliminar_conductor/<int:pk>/', EliminarConductor, name="eliminar_conductor"),
    # urls para vehiculos
    path('registrar_vehiculo/', RegistrarVehiculo, name="registrar_vehiculo"),
    path('actualizar_vehiculo/<int:pk>/', ActualizarVehiculo, name="actualizar_vehiculo"),
    path('listar_vehiculos/', ListarVehiculos, name="listar_vehiculos"),
    path('eliminar_vehiculo/<int:pk>/', EliminarVehiculo, name="eliminar_vehiculo"),

]