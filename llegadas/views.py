from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Llegada
from .forms import LlegadaForm
from pacientes.models import Paciente


@login_required
def buscar_paciente_rut(request):
    """Endpoint AJAX: devuelve nombre del paciente dado rut_numero + rut_dv."""
    rut_numero = request.GET.get('rut_numero', '').strip()
    rut_dv = request.GET.get('rut_dv', '').strip()
    if rut_numero and rut_dv:
        try:
            paciente = Paciente.objects.get(
                rut_numero=rut_numero,
                rut_dv__iexact=rut_dv,
                activo=True
            )
            return JsonResponse({'encontrado': True, 'nombre': paciente.nombre_paciente})
        except Paciente.DoesNotExist:
            pass
    return JsonResponse({'encontrado': False, 'nombre': ''})


@login_required
def llegada_lista(request):
    q = request.GET.get('q', '')
    llegadas = Llegada.objects.order_by('-creado_en')
    if q:
        llegadas = llegadas.filter(
            Q(nombre__icontains=q) |
            Q(rut_numero__icontains=q)
        )
    return render(request, 'llegadas/lista.html', {'llegadas': llegadas, 'q': q})


@login_required
def llegada_registrar(request):
    form = LlegadaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        llegada = form.save()
        messages.success(request, f'Llegada de {llegada.nombre} registrada exitosamente.')
        return redirect('llegadas:lista')
    return render(request, 'llegadas/form.html', {'form': form, 'titulo': 'Registrar Llegada'})


@login_required
def llegada_detalle(request, pk):
    llegada = get_object_or_404(Llegada, pk=pk)
    return render(request, 'llegadas/detalle.html', {'llegada': llegada})


@login_required
def llegada_editar(request, pk):
    llegada = get_object_or_404(Llegada, pk=pk)
    form = LlegadaForm(request.POST or None, instance=llegada)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Llegada actualizada exitosamente.')
        return redirect('llegadas:lista')
    return render(request, 'llegadas/form.html', {'form': form, 'titulo': 'Editar Llegada', 'objeto': llegada})


@login_required
def llegada_eliminar(request, pk):
    llegada = get_object_or_404(Llegada, pk=pk)
    if request.method == 'POST':
        llegada.delete()
        messages.success(request, 'Registro de llegada eliminado.')
        return redirect('llegadas:lista')
    return render(request, 'llegadas/confirmar_eliminar.html', {'objeto': llegada, 'titulo': 'Eliminar Llegada'})
