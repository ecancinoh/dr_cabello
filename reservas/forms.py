from django import forms
from django.contrib.auth.models import User
from .models import Reserva
from usuarios.models import PerfilUsuario


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Solo usuarios con rol DOCTOR en su perfil
        doctores_ids = PerfilUsuario.objects.filter(
            rol='DOCTOR', activo=True
        ).values_list('user_id', flat=True)
        self.fields['medico'].queryset = User.objects.filter(
            id__in=doctores_ids
        ).order_by('last_name', 'first_name')
        self.fields['medico'].label_from_instance = lambda u: u.get_full_name() or u.username
