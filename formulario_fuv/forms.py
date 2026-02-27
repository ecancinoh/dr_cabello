from django import forms
from .models import FormularioFUV


class FormularioFUVForm(forms.ModelForm):
    class Meta:
        model = FormularioFUV
        fields = [
            'paciente', 'historial', 'medico', 'fecha_evaluacion',
            'edad_meses', 'peso_kg', 'talla_cm', 'imc', 'perimetro_cefalico',
            'dpm_resultado', 'dpm_observaciones',
            'lactancia_materna', 'alimentacion_complementaria', 'alimentacion_observaciones',
            'vacunas_al_dia', 'vacunas_observaciones',
            'examenes_solicitados', 'examenes_resultados',
            'diagnostico', 'indicaciones', 'proxima_control',
        ]
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'historial': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'fecha_evaluacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'proxima_control': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'edad_meses': forms.NumberInput(attrs={'class': 'form-control'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'talla_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'imc': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'perimetro_cefalico': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'dpm_resultado': forms.Select(attrs={'class': 'form-select'}),
            'dpm_observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'alimentacion_observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'vacunas_observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'examenes_solicitados': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'examenes_resultados': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'indicaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
