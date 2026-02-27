from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from pacientes.models import Paciente
from reservas.models import Reserva
from llegadas.models import Llegada
from historial.models import HistorialPaciente
from formulario_fuv.models import FormularioFUV


@login_required
def index(request):
    hoy = date.today()
    context = {
        'total_pacientes': Paciente.objects.filter(activo=True).count(),
        'reservas_hoy': Reserva.objects.filter(fecha=hoy).count(),
        'llegadas_hoy': Llegada.objects.filter(hora_llegada__date=hoy).count(),
        'en_espera': Llegada.objects.filter(estado='ESPERANDO').count(),
        'en_atencion': Llegada.objects.filter(estado='EN_ATENCION').count(),
        'reservas_pendientes': Reserva.objects.filter(fecha=hoy, estado='PENDIENTE').order_by('hora')[:10],
        'llegadas_recientes': Llegada.objects.select_related('reserva__paciente').filter(
            hora_llegada__date=hoy
        ).order_by('-hora_llegada')[:10],
        'ultimas_reservas': Reserva.objects.select_related('paciente').order_by('-creado_en')[:5],
        'hoy': hoy,
    }
    return render(request, 'dashboard/index.html', context)
