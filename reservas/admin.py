from django.contrib import admin
from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'hora', 'tipo_consulta', 'estado', 'medico')
    list_filter = ('estado', 'tipo_consulta', 'fecha')
    search_fields = ('paciente__nombre_paciente', 'paciente__rut_numero')
    readonly_fields = ('creado_en', 'actualizado_en')
    date_hierarchy = 'fecha'
