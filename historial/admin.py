from django.contrib import admin
from .models import HistorialPaciente


@admin.register(HistorialPaciente)
class HistorialPacienteAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_consulta', 'diagnostico', 'medico')
    list_filter = ('fecha_consulta',)
    search_fields = ('paciente__nombre_paciente', 'diagnostico')
    readonly_fields = ('creado_en', 'actualizado_en')
    date_hierarchy = 'fecha_consulta'
