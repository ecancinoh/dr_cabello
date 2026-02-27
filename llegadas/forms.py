from django import forms
from .models import Llegada


class LlegadaForm(forms.ModelForm):
    class Meta:
        model = Llegada
        fields = [
            'rut_numero', 'rut_dv', 'nombre', 'tipo_llegada', 'etapa',
            'fecha', 'edad', 'peso_kg', 'talla_cm', 'cc_cm',
            'anamnesis', 'examen_fisico', 'diagnostico', 'tratamiento', 'control',
        ]
        widgets = {
            'rut_numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678'}),
            'rut_dv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'K'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_llegada': forms.Select(attrs={'class': 'form-control'}),
            'etapa': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'talla_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cc_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'anamnesis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'examen_fisico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'control': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
