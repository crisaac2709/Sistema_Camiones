from django.contrib import admin
from .models import Licencia, Chofer, Vehiculo, Marca 
   
# Register your models here.
admin.site.register(Licencia)
admin.site.register(Chofer)
admin.site.register(Vehiculo)
admin.site.register(Marca)
