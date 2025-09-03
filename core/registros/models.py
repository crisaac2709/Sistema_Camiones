from django.db import models
from vehiculos.models import Vehiculo
from cuentas.models import CustomUser

# Create your models here.
class TipoVisita(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre



class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.nombre} - {self.ruc}'
    


class Garita(models.Model):
    nombre = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.nombre}'
    

class Lugar(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    lugar_partida = models.ForeignKey(Lugar, on_delete=models.CASCADE, related_name="ruta_partida")
    lugar_destino = models.ForeignKey(Lugar, on_delete=models.CASCADE, related_name="ruta_destino")

    def __str__(self):
        return f'Lugar de partida {self.lugar_partida} - Lugar de destino {self.lugar_destino}'

    
class Registro(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    garita = models.ForeignKey(Garita, on_delete=models.CASCADE)
    guardia = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fechaHoraIngreso = models.DateTimeField(auto_now_add=True)
    fechaHoraSalida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Vehiculo {self.vehiculo.placa} - Ruta {self.ruta} - {self.garita}'