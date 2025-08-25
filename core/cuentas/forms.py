from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


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
        

    