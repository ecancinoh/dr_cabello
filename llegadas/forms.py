from django import forms
from .models import Llegada


class LlegadaForm(forms.ModelForm):
    class Meta:
        model = Llegada
        fields = ['reserva', 'estado', 'observaciones']
        widgets = {
            'reserva': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class LlegadaEstadoForm(forms.ModelForm):
    """Formulario simplificado para cambiar estado de llegada."""
    class Meta:
        model = Llegada
        fields = ['estado', 'hora_atencion', 'hora_salida', 'observaciones']
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'hora_atencion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'hora_salida': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
