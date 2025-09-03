from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vehiculo, Chofer, Licencia, Marca
from .forms import ChoferForm, VehiculoForm

# Create your views here.

#Conductor views
def RegistrarConductor(request):
    if request.method == 'POST':
        form = ChoferForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor creado correctamente')
            return redirect('vehiculos:listar_conductores')
        messages.error(request, 'Revisa algun error en el formulario')
    else:
        form = ChoferForm()
    return render(request, 'Chofer/registrar.html', {'form':form})


def ListarConductores(request):
    choferes = Chofer.objects.all()
    return render(request, 'Chofer/listar.html', {'choferes': choferes})


def ActualizarConductor(request, pk):
    chofer = get_object_or_404(Chofer, pk=pk)
    if request.method == 'POST':
        form = ChoferForm(request.POST, instance=chofer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor actualizado correctamente')
            return redirect('vehiculos:listar_conductores')
        messages.error(request, 'Revisa algun error en el formulario')
    else:
        form = ChoferForm(instance=chofer)
    return render(request, 'Chofer/registrar.html', {'form':form})



def EliminarConductor(request, pk):
    chofer = get_object_or_404(Chofer, pk=pk)
    if request.method == 'POST':
        chofer.delete()
        messages.info(request, 'Conductor eliminado correctamente')
        return redirect('vehiculos:listar_conductores')
    return render(request, 'Chofer/eliminar.html', {'chofer':chofer})


# Vehiculo views

def RegistrarVehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo creado correctamente')
            return redirect('vehiculos:listar_vehiculos')
        messages.error(request, 'Revisa algun error en el formulario')
    else:
        form = VehiculoForm()
    return render(request, 'Vehiculo/registrar.html', {'form':form})


def ListarVehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'Vehiculo/listar.html', {'vehiculos': vehiculos})


def ActualizarVehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo actualizado correctamente')
            return redirect('vehiculos:listar_vehiculos')
        messages.error(request, 'Revisa algun error en el formulario')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'Vehiculo/registrar.html', {'form':form})



def EliminarVehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        messages.info(request, 'Vehiculo eliminado correctamente')
        return redirect('vehiculos:listar_vehiculos')
    return render(request, 'Vehiculo/eliminar.html', {'vehiculo':vehiculo})