from django import forms    
from .models import Vehiculo, Chofer


class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={
                'placeholder': 'Ingresa el nombre',
                'required': True
            }),
            'apellidos': forms.TextInput(attrs={
                'placeholder': 'Ingresa el apellido',
                'required': True
            }),
            'cedula': forms.TextInput(attrs={
                'placeholder': '0932567890',
                'required': False
            }),
        }

    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres').strip()
        if nombres and len(nombres) < 3:
            raise forms.ValidationError('Minimo se necesita 3 caracteres')
        
        if nombres and not nombres.isalpha():
            raise forms.ValidationError('El nombre debe contener solo letras')
        
        return nombres
    
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos').strip()
        if apellidos and len(apellidos) < 3:
            raise forms.ValidationError('Minimo se necesita 3 caracteres')
        
        if apellidos and not apellidos.isalpha():
            raise forms.ValidationError('El apellido debe contener solo letras')
        
        return apellidos
    
    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula').strip()
        if cedula and not cedula.isdigit():
            raise forms.ValidationError('La cedula debe contener solo numeros')
        
        if cedula and not len(cedula) != 10:
            raise forms.ValidationError('Deben ser exactamente 10 digitos')
        
        return cedula
    


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'placa': forms.TextInput(attrs={
                'placeholder': 'ABC-123',
                'required': True
            })
        }

    def clean_placa(self):
        placa = self.cleaned_data.get('placa').upper().strip()
        if placa and len(placa) != 7:
            raise forms.ValidationError('La placa debe tener exactamente 7 caracteres, incluyendo el guion')
        return placa