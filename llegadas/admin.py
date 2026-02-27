from django.contrib import admin
from .models import Llegada


@admin.register(Llegada)
class LlegadaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut_completo', 'tipo_llegada', 'etapa', 'fecha', 'creado_en')
    list_filter = ('tipo_llegada', 'etapa')
    search_fields = ('nombre', 'rut_numero')
    readonly_fields = ('creado_en', 'actualizado_en')
    date_hierarchy = 'fecha'
