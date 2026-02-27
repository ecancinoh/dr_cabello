from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from pacientes.models import Paciente
from reservas.models import Reserva
from llegadas.models import Llegada
from historial.models import HistorialPaciente


@login_required
def index(request):
    hoy = date.today()
    context = {
        'total_pacientes': Paciente.objects.filter(activo=True).count(),
        'reservas_hoy': Reserva.objects.filter(fecha=hoy).count(),
        'llegadas_hoy': Llegada.objects.filter(creado_en__date=hoy).count(),
        'total_llegadas': Llegada.objects.count(),
        'reservas_pendientes': Reserva.objects.filter(fecha=hoy, estado='PENDIENTE').order_by('hora')[:10],
        'llegadas_recientes': Llegada.objects.filter(
            creado_en__date=hoy
        ).order_by('-creado_en')[:10],
        'ultimas_reservas': Reserva.objects.select_related('paciente').order_by('-creado_en')[:5],
        'hoy': hoy,
    }
    return render(request, 'dashboard/index.html', context)
