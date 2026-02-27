from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import HistorialPaciente
from .forms import HistorialForm
from pacientes.models import Paciente


@login_required
def historial_lista(request):
    q = request.GET.get('q', '')
    paciente_id = request.GET.get('paciente', '')
    historiales = HistorialPaciente.objects.select_related('paciente', 'medico').order_by('-fecha_consulta')
    if q:
        historiales = historiales.filter(
            Q(paciente__nombre_paciente__icontains=q) |
            Q(diagnostico__icontains=q)
        )
    if paciente_id:
        historiales = historiales.filter(paciente_id=paciente_id)
    return render(request, 'historial/lista.html', {'historiales': historiales, 'q': q})


@login_required
def historial_crear(request):
    initial = {}
    paciente_id = request.GET.get('paciente_id')
    if paciente_id:
        initial['paciente'] = paciente_id
    form = HistorialForm(request.POST or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        historial = form.save(commit=False)
        historial.medico = request.user
        historial.save()
        messages.success(request, 'Historial registrado exitosamente.')
        return redirect('historial:detalle', pk=historial.pk)
    return render(request, 'historial/form.html', {'form': form, 'titulo': 'Nuevo Historial'})


@login_required
def historial_detalle(request, pk):
    historial = get_object_or_404(HistorialPaciente, pk=pk)
    return render(request, 'historial/detalle.html', {'historial': historial})


@login_required
def historial_editar(request, pk):
    historial = get_object_or_404(HistorialPaciente, pk=pk)
    form = HistorialForm(request.POST or None, instance=historial)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Historial actualizado.')
        return redirect('historial:detalle', pk=historial.pk)
    return render(request, 'historial/form.html', {'form': form, 'titulo': 'Editar Historial', 'objeto': historial})


@login_required
def historial_eliminar(request, pk):
    historial = get_object_or_404(HistorialPaciente, pk=pk)
    if request.method == 'POST':
        historial.delete()
        messages.success(request, 'Historial eliminado.')
        return redirect('historial:lista')
    return render(request, 'historial/confirmar_eliminar.html', {'objeto': historial, 'titulo': 'Eliminar Historial'})
