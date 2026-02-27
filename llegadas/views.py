from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Llegada
from .forms import LlegadaForm, LlegadaEstadoForm
from reservas.models import Reserva


@login_required
def llegada_lista(request):
    q = request.GET.get('q', '')
    llegadas = Llegada.objects.select_related('reserva__paciente').order_by('-hora_llegada')
    if q:
        llegadas = llegadas.filter(
            Q(reserva__paciente__nombre_paciente__icontains=q) |
            Q(reserva__paciente__rut_numero__icontains=q)
        )
    return render(request, 'llegadas/lista.html', {'llegadas': llegadas, 'q': q})


@login_required
def llegada_registrar(request):
    """Registra la llegada de un paciente (puede venir con reserva_id en GET)."""
    initial = {}
    reserva_id = request.GET.get('reserva_id')
    if reserva_id:
        initial['reserva'] = reserva_id
    form = LlegadaForm(request.POST or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        llegada = form.save(commit=False)
        llegada.registrado_por = request.user
        llegada.save()
        # Actualiza estado de reserva
        llegada.reserva.estado = 'CONFIRMADA'
        llegada.reserva.save()
        messages.success(request, f'Llegada registrada para {llegada.reserva.paciente}.')
        return redirect('llegadas:lista')
    return render(request, 'llegadas/form.html', {'form': form, 'titulo': 'Registrar Llegada'})


@login_required
def llegada_detalle(request, pk):
    llegada = get_object_or_404(Llegada, pk=pk)
    return render(request, 'llegadas/detalle.html', {'llegada': llegada})


@login_required
def llegada_editar(request, pk):
    llegada = get_object_or_404(Llegada, pk=pk)
    form = LlegadaEstadoForm(request.POST or None, instance=llegada)
    if request.method == 'POST' and form.is_valid():
        llegada = form.save(commit=False)
        if llegada.estado == 'EN_ATENCION' and not llegada.hora_atencion:
            llegada.hora_atencion = timezone.now()
        if llegada.estado == 'ATENDIDO' and not llegada.hora_salida:
            llegada.hora_salida = timezone.now()
        llegada.save()
        messages.success(request, 'Estado de llegada actualizado.')
        return redirect('llegadas:lista')
    return render(request, 'llegadas/form.html', {'form': form, 'titulo': 'Actualizar Llegada', 'objeto': llegada})


@login_required
def llegada_eliminar(request, pk):
    llegada = get_object_or_404(Llegada, pk=pk)
    if request.method == 'POST':
        llegada.delete()
        messages.success(request, 'Registro de llegada eliminado.')
        return redirect('llegadas:lista')
    return render(request, 'llegadas/confirmar_eliminar.html', {'objeto': llegada, 'titulo': 'Eliminar Llegada'})
