from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'rut_numero', 'rut_dv', 'nombre_paciente', 'sexo', 'fecha_nacimiento',
            'celular', 'direccion', 'comuna', 'ciudad', 'prevision',
            'nombre_mama', 'nombre_papa',
            'parto', 'peso_kg', 'talla_cm', 'cc_cm', 'apgar',
            'edad_gestacional_semanas', 'grupo_sanguineo_abo', 'grupo_sanguineo_rh',
            'activo',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'rut_numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678'}),
            'rut_dv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'K'}),
            'nombre_paciente': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_mama': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_papa': forms.TextInput(attrs={'class': 'form-control'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'talla_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cc_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'apgar': forms.NumberInput(attrs={'class': 'form-control'}),
            'edad_gestacional_semanas': forms.NumberInput(attrs={'class': 'form-control'}),
            'prevision': forms.Select(attrs={'class': 'form-select'}),
            'parto': forms.Select(attrs={'class': 'form-select'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
            'grupo_sanguineo_abo': forms.Select(attrs={'class': 'form-select'}),
            'grupo_sanguineo_rh': forms.Select(attrs={'class': 'form-select'}),
        }
