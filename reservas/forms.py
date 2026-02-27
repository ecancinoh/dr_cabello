from django import forms
from .models import Reserva
from pacientes.models import Paciente


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'paciente', 'medico', 'fecha', 'hora',
            'tipo_consulta', 'estado', 'motivo_consulta', 'observaciones',
        ]
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'tipo_consulta': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'motivo_consulta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
