from django.contrib import admin
from .models import FormularioFUV


@admin.register(FormularioFUV)
class FormularioFUVAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_evaluacion', 'dpm_resultado', 'medico')
    list_filter = ('dpm_resultado', 'vacunas_al_dia', 'lactancia_materna')
    search_fields = ('paciente__nombre_paciente', 'diagnostico')
    readonly_fields = ('creado_en', 'actualizado_en')
    date_hierarchy = 'fecha_evaluacion'
