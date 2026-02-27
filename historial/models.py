from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente
from reservas.models import Reserva


class HistorialPaciente(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name='historial',
        verbose_name='Paciente'
    )
    reserva = models.OneToOneField(
        Reserva,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='historial',
        verbose_name='Reserva Asociada'
    )
    medico = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='historiales_atendidos',
        verbose_name='Médico'
    )
    fecha_consulta = models.DateField('Fecha de Consulta')
    motivo_consulta = models.TextField('Motivo de Consulta')
    anamnesis = models.TextField('Anamnesis', blank=True, null=True)
    examen_fisico = models.TextField('Examen Físico', blank=True, null=True)
    diagnostico = models.TextField('Diagnóstico')
    indicaciones = models.TextField('Indicaciones', blank=True, null=True)
    receta = models.TextField('Receta/Medicamentos', blank=True, null=True)
    proxima_cita = models.DateField('Próxima Cita', blank=True, null=True)
    # Signos vitales al momento de la consulta
    peso_kg = models.DecimalField('Peso (Kg)', max_digits=5, decimal_places=2, blank=True, null=True)
    talla_cm = models.DecimalField('Talla (cm)', max_digits=5, decimal_places=2, blank=True, null=True)
    temperatura = models.DecimalField('Temperatura (°C)', max_digits=4, decimal_places=1, blank=True, null=True)
    frecuencia_cardiaca = models.PositiveSmallIntegerField('Frec. Cardíaca (lpm)', blank=True, null=True)
    saturacion_oxigeno = models.PositiveSmallIntegerField('Saturación O₂ (%)', blank=True, null=True)
    creado_en = models.DateTimeField('Creado en', auto_now_add=True)
    actualizado_en = models.DateTimeField('Actualizado en', auto_now=True)

    class Meta:
        verbose_name = 'Historial del Paciente'
        verbose_name_plural = 'Historial de Pacientes'
        ordering = ['-fecha_consulta']

    def __str__(self):
        return f'Historial {self.paciente} – {self.fecha_consulta}'
