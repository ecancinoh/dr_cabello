from django.contrib import admin
from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_paciente', 'rut_completo', 'fecha_nacimiento', 'prevision', 'activo')
    list_filter = ('prevision', 'activo', 'parto')
    search_fields = ('nombre_paciente', 'rut_numero')
    readonly_fields = ('creado_en', 'actualizado_en')
