from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'Administrador'),
        ('guardia', 'Guardia'),
    ]
    cedula = models.CharField(max_length=10, unique=True, null=True)
    foto = models.ImageField(upload_to='cuentas/', null=True, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='guardia')
