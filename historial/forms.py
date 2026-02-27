from django import forms
from .models import HistorialPaciente


class HistorialForm(forms.ModelForm):
    class Meta:
        model = HistorialPaciente
        fields = [
            'paciente', 'reserva', 'medico', 'fecha_consulta',
            'motivo_consulta', 'anamnesis', 'examen_fisico',
            'diagnostico', 'indicaciones', 'receta', 'proxima_cita',
            'peso_kg', 'talla_cm', 'temperatura',
            'frecuencia_cardiaca', 'saturacion_oxigeno',
        ]
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'reserva': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'fecha_consulta': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'proxima_cita': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'motivo_consulta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'anamnesis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'examen_fisico': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'indicaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'receta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'talla_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'temperatura': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'frecuencia_cardiaca': forms.NumberInput(attrs={'class': 'form-control'}),
            'saturacion_oxigeno': forms.NumberInput(attrs={'class': 'form-control'}),
        }
