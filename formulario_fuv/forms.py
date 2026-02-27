from django import forms
from .models import EvaluacionSalud


class EvaluacionSaludForm(forms.ModelForm):
    class Meta:
        model = EvaluacionSalud
        fields = [
            'run_numero', 'run_dv', 'nombres_apellidos', 'sexo',
            'fecha_nacimiento', 'edad_anios_meses', 'nacionalidad',
            'lengua_familia_origen', 'lengua_habitual', 'fecha_reevaluacion',
            'peso_kg', 'talla_cm', 'imc',
            'diagnostico', 'indicaciones',
        ]
        widgets = {
            'run_numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678'}),
            'run_dv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'K', 'maxlength': '1', 'style': 'text-transform:uppercase'}),
            'nombres_apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'edad_anios_meses': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3a 2m'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'lengua_familia_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'lengua_habitual': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_reevaluacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'talla_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'imc': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'indicaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
