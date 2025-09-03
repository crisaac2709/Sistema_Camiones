from django.db import models

# Create your models here.
class Licencia(models.Model):
    nombre = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.nombre
    


class Chofer(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True, null=True)
    licencia = models.ForeignKey(Licencia, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Chofer'
        verbose_name_plural = 'Choferes'
        ordering = ['apellidos']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    

class Marca(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre
    
    

class Vehiculo(models.Model):
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Vehiculo: {self.placa}'
