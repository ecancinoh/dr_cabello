from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Paciente
from .forms import PacienteForm


@login_required
def paciente_lista(request):
    q = request.GET.get('q', '')
    pacientes = Paciente.objects.filter(activo=True)
    if q:
        pacientes = pacientes.filter(
            Q(nombre_paciente__icontains=q) |
            Q(rut_numero__icontains=q)
        )
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes, 'q': q})


@login_required
def paciente_crear(request):
    form = PacienteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Paciente creado exitosamente.')
        return redirect('pacientes:lista')
    return render(request, 'pacientes/form.html', {'form': form, 'titulo': 'Nuevo Paciente'})


@login_required
def paciente_detalle(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'pacientes/detalle.html', {'paciente': paciente})


@login_required
def paciente_editar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    form = PacienteForm(request.POST or None, instance=paciente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Paciente actualizado exitosamente.')
        return redirect('pacientes:detalle', pk=paciente.pk)
    return render(request, 'pacientes/form.html', {'form': form, 'titulo': 'Editar Paciente', 'objeto': paciente})


@login_required
def paciente_eliminar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.activo = False
        paciente.save()
        messages.success(request, 'Paciente desactivado.')
        return redirect('pacientes:lista')
    return render(request, 'pacientes/confirmar_eliminar.html', {'objeto': paciente, 'titulo': 'Desactivar Paciente'})
