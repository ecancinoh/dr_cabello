from django.contrib import admin
from .models import Llegada


@admin.register(Llegada)
class LlegadaAdmin(admin.ModelAdmin):
    list_display = ('reserva', 'hora_llegada', 'estado', 'registrado_por')
    list_filter = ('estado',)
    search_fields = ('reserva__paciente__nombre_paciente',)
    readonly_fields = ('hora_llegada',)
