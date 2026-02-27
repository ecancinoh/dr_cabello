from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import EvaluacionSalud
from .forms import EvaluacionSaludForm


@login_required
def fuv_lista(request):
    q = request.GET.get('q', '')
    evaluaciones = EvaluacionSalud.objects.order_by('-creado_en')
    if q:
        evaluaciones = evaluaciones.filter(
            Q(nombres_apellidos__icontains=q) |
            Q(run_numero__icontains=q)
        )
    return render(request, 'formulario_fuv/lista.html', {'evaluaciones': evaluaciones, 'q': q})


@login_required
def fuv_crear(request):
    form = EvaluacionSaludForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ev = form.save()
        messages.success(request, 'Evaluación de Salud creada exitosamente.')
        return redirect('formulario_fuv:detalle', pk=ev.pk)
    return render(request, 'formulario_fuv/form.html', {'form': form, 'titulo': 'Nueva Evaluación de Salud'})


@login_required
def fuv_detalle(request, pk):
    ev = get_object_or_404(EvaluacionSalud, pk=pk)
    return render(request, 'formulario_fuv/detalle.html', {'ev': ev})


@login_required
def fuv_editar(request, pk):
    ev = get_object_or_404(EvaluacionSalud, pk=pk)
    form = EvaluacionSaludForm(request.POST or None, instance=ev)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Evaluación de Salud actualizada.')
        return redirect('formulario_fuv:detalle', pk=ev.pk)
    return render(request, 'formulario_fuv/form.html', {'form': form, 'titulo': 'Editar Evaluación de Salud', 'objeto': ev})


@login_required
def fuv_eliminar(request, pk):
    ev = get_object_or_404(EvaluacionSalud, pk=pk)
    if request.method == 'POST':
        ev.delete()
        messages.success(request, 'Evaluación de Salud eliminada.')
        return redirect('formulario_fuv:lista')
    return render(request, 'formulario_fuv/confirmar_eliminar.html', {'objeto': ev, 'titulo': 'Eliminar Evaluación de Salud'})
