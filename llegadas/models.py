from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Llegada(models.Model):
    # ---------------------------
    # Validadores RUT
    # ---------------------------
    rut_numero_validator = RegexValidator(
        regex=r'^\d{1,8}$',
        message='El RUT debe tener entre 1 y 8 dígitos (sin puntos).'
    )
    rut_dv_validator = RegexValidator(
        regex=r'^[0-9Kk]{1}$',
        message='El dígito verificador debe ser 0-9 o K.'
    )

    # ---------------------------
    # Choices
    # ---------------------------
    TIPO_LLEGADA_CHOICES = [
        ('CONTROL', 'Control'),
        ('ENFERMEDAD', 'Enfermedad'),
        ('CONTROL_ENFERMEDAD', 'Control de Enfermedad'),
    ]

    ETAPA_CHOICES = [
        ('INGRESO', 'Ingreso'),
        ('EVALUACION', 'Evaluación'),
        ('TRATAMIENTO', 'Tratamiento'),
        ('ALTA', 'Alta'),
        ('OTRA', 'Otra'),
    ]

    # ---------------------------
    # Campos
    # ---------------------------
    rut_numero = models.CharField(
        'RUT (número)', max_length=8,
        validators=[rut_numero_validator],
        help_text='Sin puntos ni guión. Ej: 12345678'
    )
    rut_dv = models.CharField(
        'DV', max_length=1,
        validators=[rut_dv_validator],
        help_text='0-9 o K'
    )
    nombre = models.CharField('Nombre', max_length=150)
    tipo_llegada = models.CharField(
        'Tipo Llegada', max_length=30,
        choices=TIPO_LLEGADA_CHOICES, blank=True, null=True
    )
    etapa = models.CharField(
        'Etapa', max_length=30,
        choices=ETAPA_CHOICES, blank=True, null=True
    )
    fecha = models.DateField('Fecha', blank=True, null=True)
    edad = models.PositiveSmallIntegerField(
        'Edad', blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(150)]
    )
    peso_kg = models.DecimalField(
        'Peso (Kg)', max_digits=6, decimal_places=2, blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )
    talla_cm = models.DecimalField(
        'Talla (cm)', max_digits=6, decimal_places=2, blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(250)]
    )
    cc_cm = models.DecimalField(
        'C.C. (cm)', max_digits=6, decimal_places=2, blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    anamnesis = models.TextField('Anamnesis', blank=True, null=True)
    examen_fisico = models.TextField('Examen Físico', blank=True, null=True)
    diagnostico = models.TextField('Diagnóstico', blank=True, null=True)
    tratamiento = models.TextField('Tratamiento', blank=True, null=True)
    control = models.TextField('Control', blank=True, null=True)
    creado_en = models.DateTimeField('Creado en', auto_now_add=True)
    actualizado_en = models.DateTimeField('Actualizado en', auto_now=True)

    class Meta:
        verbose_name = 'Llegada'
        verbose_name_plural = 'Llegadas'
        ordering = ['-creado_en']
        indexes = [
            models.Index(fields=['rut_numero', 'rut_dv']),
            models.Index(fields=['fecha']),
            models.Index(fields=['nombre']),
        ]

    def __str__(self):
        return f'{self.nombre} - {self.rut_completo} ({self.fecha or "sin fecha"})'

    @property
    def rut_completo(self):
        return f'{self.rut_numero}-{self.rut_dv.upper()}'
