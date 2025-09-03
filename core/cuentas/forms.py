from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
import os

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('foto', 'telefono', 'fecha_nacimiento', 'cedula', 'rol')
        
    def clean_cedula(self):
        cedula = (self.cleaned_data.get("cedula") or "").strip()
        if not cedula.isdigit() or len(cedula) != 10:
            raise forms.ValidationError('La cedula debe tener 10 digitos')
        return cedula
        
    def clean_telefono(self):
        telefono = (self.cleaned_data.get("telefono") or "").strip()
        if telefono and (not telefono.isdigit() or len(telefono) != 10):
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return telefono

    def clean_foto(self):
        archivo = self.cleaned_data.get('foto')

        if not archivo:
            return archivo
        
        # Obtenemos el nombre del archivo (foto)
        nombre_archivo = archivo.name.lower().strip()

        # Obtenemos la extension
        extension = os.path.splitext(nombre_archivo)[1]
        extensiones_permitidas = ('.jpg', '.png', '.jpeg')

        if extension not in extensiones_permitidas:
            raise forms.ValidationError('Solo se permiten fotos en formato .png, .jpg o .jpeg')

        peso_maximo = 2 * 1024 * 1024
        if archivo.size > peso_maximo:
            raise forms.ValidationError('El peso maximo es de 2 MB')

        return archivo        
    

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        from datetime import date
        hoy = date.today()

        edad = hoy.year - fecha_nacimiento.year

        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1

        if edad < 18:
            raise forms.ValidationError('Debe tener minimo 18 años para registrarse')

        return fecha_nacimiento