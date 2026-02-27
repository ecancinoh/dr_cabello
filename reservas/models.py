from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente


class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('ATENDIDA', 'Atendida'),
        ('NO_ASISTIO', 'No Asistió'),
    ]

    TIPO_CONSULTA_CHOICES = [
        ('CONTROL', 'Control'),
        ('MORBILIDAD', 'Morbilidad'),
        ('URGENCIA', 'Urgencia'),
        ('PROCEDIMIENTO', 'Procedimiento'),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name='reservas',
        verbose_name='Paciente'
    )
    medico = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reservas_medico',
        verbose_name='Médico'
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reservas_creadas',
        verbose_name='Creado por'
    )
    fecha = models.DateField('Fecha')
    hora = models.TimeField('Hora')
    tipo_consulta = models.CharField('Tipo de Consulta', max_length=20, choices=TIPO_CONSULTA_CHOICES, default='CONTROL')
    estado = models.CharField('Estado', max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    motivo_consulta = models.TextField('Motivo de Consulta', blank=True, null=True)
    observaciones = models.TextField('Observaciones', blank=True, null=True)
    creado_en = models.DateTimeField('Creado en', auto_now_add=True)
    actualizado_en = models.DateTimeField('Actualizado en', auto_now=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['fecha', 'hora']

    def __str__(self):
        return f'{self.paciente} – {self.fecha} {self.hora}'
