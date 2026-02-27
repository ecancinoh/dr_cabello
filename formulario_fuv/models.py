from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente
from historial.models import HistorialPaciente


class FormularioFUV(models.Model):
    """Formulario Único Valorización de Salud – Chile."""

    RESULTADO_CHOICES = [
        ('NORMAL', 'Normal'),
        ('RIESGO', 'Riesgo'),
        ('RETRASO', 'Retraso'),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name='formularios_fuv',
        verbose_name='Paciente'
    )
    historial = models.OneToOneField(
        HistorialPaciente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='formulario_fuv',
        verbose_name='Historial Asociado'
    )
    medico = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='formularios_fuv',
        verbose_name='Médico'
    )
    fecha_evaluacion = models.DateField('Fecha de Evaluación')
    # ---- Datos antropométricos ----
    edad_meses = models.PositiveSmallIntegerField('Edad (meses)', blank=True, null=True)
    peso_kg = models.DecimalField('Peso (Kg)', max_digits=5, decimal_places=2, blank=True, null=True)
    talla_cm = models.DecimalField('Talla (cm)', max_digits=5, decimal_places=2, blank=True, null=True)
    imc = models.DecimalField('IMC', max_digits=5, decimal_places=2, blank=True, null=True)
    perimetro_cefalico = models.DecimalField('Perímetro Cefálico (cm)', max_digits=5, decimal_places=2, blank=True, null=True)
    # ---- Desarrollo psicomotor ----
    dpm_resultado = models.CharField('Resultado DSM', max_length=20, choices=RESULTADO_CHOICES, blank=True, null=True)
    dpm_observaciones = models.TextField('Observaciones DSM', blank=True, null=True)
    # ---- Alimentación ----
    lactancia_materna = models.BooleanField('Lactancia Materna', default=False)
    alimentacion_complementaria = models.BooleanField('Alimentación Complementaria', default=False)
    alimentacion_observaciones = models.TextField('Obs. Alimentación', blank=True, null=True)
    # ---- Vacunas ----
    vacunas_al_dia = models.BooleanField('Vacunas al Día', default=False)
    vacunas_observaciones = models.TextField('Obs. Vacunas', blank=True, null=True)
    # ---- Exámenes ----
    examenes_solicitados = models.TextField('Exámenes Solicitados', blank=True, null=True)
    examenes_resultados = models.TextField('Resultados Exámenes', blank=True, null=True)
    # ---- Diagnóstico y plan ----
    diagnostico = models.TextField('Diagnóstico')
    indicaciones = models.TextField('Indicaciones', blank=True, null=True)
    proxima_control = models.DateField('Próximo Control', blank=True, null=True)
    # ---- Metadatos ----
    creado_en = models.DateTimeField('Creado en', auto_now_add=True)
    actualizado_en = models.DateTimeField('Actualizado en', auto_now=True)

    class Meta:
        verbose_name = 'Formulario FUV'
        verbose_name_plural = 'Formularios FUV'
        ordering = ['-fecha_evaluacion']

    def __str__(self):
        return f'FUV – {self.paciente} – {self.fecha_evaluacion}'
