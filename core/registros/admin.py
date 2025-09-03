from django.contrib import admin
from .models import Empresa, TipoVisita, Garita, Registro, Lugar, Ruta

# Register your models here.
admin.site.register(Empresa)
admin.site.register(TipoVisita)
admin.site.register(Garita)
admin.site.register(Registro)
admin.site.register(Lugar)
admin.site.register(Ruta)
