from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Paciente(models.Model):
    # ---------------------------
    # Validadores
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
    PREVISION_CHOICES = [
        ('FONASA', 'FONASA'),
        ('ISAPRE', 'ISAPRE'),
        ('PARTICULAR', 'Particular'),
        ('OTRA', 'Otra'),
    ]
    PARTO_CHOICES = [
        ('VAGINAL', 'Vaginal'),
        ('CESAREA', 'Cesárea'),
        ('INSTRUMENTAL', 'Instrumental'),
        ('OTRO', 'Otro'),
    ]
    ABO_CHOICES = [
        ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O'),
    ]
    RH_CHOICES = [
        ('+', 'Rh +'), ('-', 'Rh -'),
    ]
    COMUNA_CHOICES = [
        # Provincia de Cachapoal
        ('RANCAGUA', 'Rancagua'),
        ('CODEGUA', 'Codegua'),
        ('COINCO', 'Coínco'),
        ('COLTAUCO', 'Coltauco'),
        ('DONIHUE', 'Doñihue'),
        ('GRANEROS', 'Graneros'),
        ('LAS_CABRAS', 'Las Cabras'),
        ('MACHALI', 'Machalí'),
        ('MALLOA', 'Malloa'),
        ('MOSTAZAL', 'Mostazal'),
        ('OLIVAR', 'Olivar'),
        ('PEUMO', 'Peumo'),
        ('PICHIDEGUA', 'Pichidegua'),
        ('QUINTA_DE_TILCOCO', 'Quinta de Tilcoco'),
        ('RENGO', 'Rengo'),
        ('REQUINOA', 'Requínoa'),
        ('SAN_VICENTE', 'San Vicente de Tagua Tagua'),
        # Provincia de Colchagua
        ('SAN_FERNANDO', 'San Fernando'),
        ('CHEPICA', 'Chépica'),
        ('CHIMBARONGO', 'Chimbarongo'),
        ('LOLOL', 'Lolol'),
        ('NANCAGUA', 'Nancagua'),
        ('PALMILLA', 'Palmilla'),
        ('PERALILLO', 'Peralillo'),
        ('PLACILLA', 'Placilla'),
        ('PUMANQUE', 'Pumanque'),
        ('SANTA_CRUZ', 'Santa Cruz'),
        # Provincia de Cardenal Caro
        ('PICHILEMU', 'Pichilemu'),
        ('LA_ESTRELLA', 'La Estrella'),
        ('LITUECHE', 'Litueche'),
        ('MARCHIHUE', 'Marchihue'),
        ('NAVIDAD', 'Navidad'),
        ('PAREDONES', 'Paredones'),
    ]

    # ---------------------------
    # Campos
    # ---------------------------
    rut_numero = models.CharField('RUT (número)', max_length=8, validators=[rut_numero_validator], help_text='Sin puntos ni guión. Ej: 12345678')
    rut_dv = models.CharField('DV', max_length=1, validators=[rut_dv_validator], help_text='0-9 o K')
    nombre_paciente = models.CharField('Nombre Paciente', max_length=150)
    direccion = models.CharField('Dirección', max_length=255, blank=True, null=True)
    comuna = models.CharField('Comuna', max_length=50, choices=COMUNA_CHOICES, blank=True, null=True)
    ciudad = models.CharField('Ciudad', max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField('Fecha Nacimiento', blank=True, null=True)
    celular = models.CharField('Celular', max_length=20, blank=True, null=True)
    prevision = models.CharField('Previsión', max_length=20, choices=PREVISION_CHOICES, blank=True, null=True)
    nombre_mama = models.CharField('Nombre Mamá', max_length=150, blank=True, null=True)
    nombre_papa = models.CharField('Nombre Papá', max_length=150, blank=True, null=True)
    parto = models.CharField('Parto', max_length=20, choices=PARTO_CHOICES, blank=True, null=True)
    peso_kg = models.DecimalField('Peso (Kg)', max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    talla_cm = models.DecimalField('Talla (cm)', max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(120)])
    cc_cm = models.DecimalField('C.C. (cm)', max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(80)])
    apgar = models.PositiveSmallIntegerField('Apgar', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    edad_gestacional_semanas = models.PositiveSmallIntegerField('Edad Gestacional (semanas)', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(45)])
    grupo_sanguineo_abo = models.CharField('Grupo Sanguíneo (ABO)', max_length=2, choices=ABO_CHOICES, blank=True, null=True)
    grupo_sanguineo_rh = models.CharField('Factor Rh', max_length=1, choices=RH_CHOICES, blank=True, null=True)
    activo = models.BooleanField('Activo', default=True)
    creado_en = models.DateTimeField('Creado en', auto_now_add=True)
    actualizado_en = models.DateTimeField('Actualizado en', auto_now=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        constraints = [
            models.UniqueConstraint(fields=['rut_numero', 'rut_dv'], name='uq_paciente_rut'),
        ]

    def __str__(self):
        return f'{self.nombre_paciente} ({self.rut_completo})'

    @property
    def rut_completo(self):
        return f'{self.rut_numero}-{self.rut_dv.upper()}'
