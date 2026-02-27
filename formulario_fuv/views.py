from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import FormularioFUV
from .forms import FormularioFUVForm


@login_required
def fuv_lista(request):
    q = request.GET.get('q', '')
    formularios = FormularioFUV.objects.select_related('paciente', 'medico').order_by('-fecha_evaluacion')
    if q:
        formularios = formularios.filter(
            Q(paciente__nombre_paciente__icontains=q) |
            Q(paciente__rut_numero__icontains=q)
        )
    return render(request, 'formulario_fuv/lista.html', {'formularios': formularios, 'q': q})


@login_required
def fuv_crear(request):
    initial = {}
    paciente_id = request.GET.get('paciente_id')
    historial_id = request.GET.get('historial_id')
    if paciente_id:
        initial['paciente'] = paciente_id
    if historial_id:
        initial['historial'] = historial_id
    form = FormularioFUVForm(request.POST or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        fuv = form.save(commit=False)
        fuv.medico = request.user
        fuv.save()
        messages.success(request, 'Formulario FUV creado exitosamente.')
        return redirect('formulario_fuv:detalle', pk=fuv.pk)
    return render(request, 'formulario_fuv/form.html', {'form': form, 'titulo': 'Nuevo Formulario FUV'})


@login_required
def fuv_detalle(request, pk):
    fuv = get_object_or_404(FormularioFUV, pk=pk)
    return render(request, 'formulario_fuv/detalle.html', {'fuv': fuv})


@login_required
def fuv_editar(request, pk):
    fuv = get_object_or_404(FormularioFUV, pk=pk)
    form = FormularioFUVForm(request.POST or None, instance=fuv)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Formulario FUV actualizado.')
        return redirect('formulario_fuv:detalle', pk=fuv.pk)
    return render(request, 'formulario_fuv/form.html', {'form': form, 'titulo': 'Editar Formulario FUV', 'objeto': fuv})


@login_required
def fuv_eliminar(request, pk):
    fuv = get_object_or_404(FormularioFUV, pk=pk)
    if request.method == 'POST':
        fuv.delete()
        messages.success(request, 'Formulario FUV eliminado.')
        return redirect('formulario_fuv:lista')
    return render(request, 'formulario_fuv/confirmar_eliminar.html', {'objeto': fuv, 'titulo': 'Eliminar Formulario FUV'})
