from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Reserva
from .forms import ReservaForm


@login_required
def reserva_lista(request):
    q = request.GET.get('q', '')
    fecha = request.GET.get('fecha', '')
    reservas = Reserva.objects.select_related('paciente', 'medico').order_by('fecha', 'hora')
    if q:
        reservas = reservas.filter(
            Q(paciente__nombre_paciente__icontains=q) |
            Q(paciente__rut_numero__icontains=q)
        )
    if fecha:
        reservas = reservas.filter(fecha=fecha)
    return render(request, 'reservas/lista.html', {'reservas': reservas, 'q': q, 'fecha': fecha})


@login_required
def reserva_crear(request):
    form = ReservaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        reserva = form.save(commit=False)
        reserva.creado_por = request.user
        reserva.save()
        messages.success(request, 'Reserva creada exitosamente.')
        return redirect('reservas:lista')
    return render(request, 'reservas/form.html', {'form': form, 'titulo': 'Nueva Reserva'})


@login_required
def reserva_detalle(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reservas/detalle.html', {'reserva': reserva})


@login_required
def reserva_editar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    form = ReservaForm(request.POST or None, instance=reserva)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Reserva actualizada exitosamente.')
        return redirect('reservas:lista')
    return render(request, 'reservas/form.html', {'form': form, 'titulo': 'Editar Reserva', 'objeto': reserva})


@login_required
def reserva_eliminar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.estado = 'CANCELADA'
        reserva.save()
        messages.success(request, 'Reserva cancelada.')
        return redirect('reservas:lista')
    return render(request, 'reservas/confirmar_eliminar.html', {'objeto': reserva, 'titulo': 'Cancelar Reserva'})
