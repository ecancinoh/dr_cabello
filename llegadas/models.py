from django.db import models
from django.contrib.auth.models import User
from reservas.models import Reserva


class Llegada(models.Model):
    ESTADO_CHOICES = [
        ('ESPERANDO', 'Esperando'),
        ('EN_ATENCION', 'En Atención'),
        ('ATENDIDO', 'Atendido'),
    ]

    reserva = models.OneToOneField(
        Reserva,
        on_delete=models.PROTECT,
        related_name='llegada',
        verbose_name='Reserva'
    )
    hora_llegada = models.DateTimeField('Hora de Llegada', auto_now_add=True)
    hora_atencion = models.DateTimeField('Hora de Atención', blank=True, null=True)
    hora_salida = models.DateTimeField('Hora de Salida', blank=True, null=True)
    estado = models.CharField('Estado', max_length=20, choices=ESTADO_CHOICES, default='ESPERANDO')
    registrado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='llegadas_registradas',
        verbose_name='Registrado por'
    )
    observaciones = models.TextField('Observaciones', blank=True, null=True)

    class Meta:
        verbose_name = 'Llegada'
        verbose_name_plural = 'Llegadas'
        ordering = ['-hora_llegada']

    def __str__(self):
        return f'Llegada de {self.reserva.paciente} – {self.hora_llegada.strftime("%d/%m/%Y %H:%M")}'
