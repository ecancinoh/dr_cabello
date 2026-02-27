from django.contrib import admin
from .models import EvaluacionSalud


@admin.register(EvaluacionSalud)
class EvaluacionSaludAdmin(admin.ModelAdmin):
    list_display = ('nombres_apellidos', 'run_completo', 'sexo', 'fecha_nacimiento', 'fecha_reevaluacion', 'creado_en')
    list_filter = ('sexo',)
    search_fields = ('nombres_apellidos', 'run_numero', 'diagnostico')
    readonly_fields = ('creado_en', 'actualizado_en')
    date_hierarchy = 'creado_en'
