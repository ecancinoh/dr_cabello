from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import PerfilUsuario
from .forms import UsuarioCrearForm, PerfilUsuarioForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard:index')
    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('usuarios:login')


@login_required
def usuario_lista(request):
    usuarios = PerfilUsuario.objects.select_related('user').all().order_by('user__last_name')
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


@login_required
def usuario_crear(request):
    form = UsuarioCrearForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Usuario creado exitosamente.')
        return redirect('usuarios:lista')
    return render(request, 'usuarios/form.html', {'form': form, 'titulo': 'Nuevo Usuario'})


@login_required
def usuario_editar(request, pk):
    perfil = get_object_or_404(PerfilUsuario, pk=pk)
    form = PerfilUsuarioForm(request.POST or None, instance=perfil)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Usuario actualizado exitosamente.')
        return redirect('usuarios:lista')
    return render(request, 'usuarios/form.html', {'form': form, 'titulo': 'Editar Usuario', 'objeto': perfil})


@login_required
def usuario_eliminar(request, pk):
    perfil = get_object_or_404(PerfilUsuario, pk=pk)
    if request.method == 'POST':
        perfil.user.delete()
        messages.success(request, 'Usuario eliminado.')
        return redirect('usuarios:lista')
    return render(request, 'usuarios/confirmar_eliminar.html', {'objeto': perfil, 'titulo': 'Eliminar Usuario'})


@login_required
def usuario_detalle(request, pk):
    perfil = get_object_or_404(PerfilUsuario, pk=pk)
    return render(request, 'usuarios/detalle.html', {'perfil': perfil})
