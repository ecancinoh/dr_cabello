from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class EvaluacionSalud(models.Model):
    """Formulario Único Valorización de Salud – Chile."""

    # ---------------------------
    # Validadores RUN/RUT (sin puntos)
    # ---------------------------
    run_numero_validator = RegexValidator(
        regex=r"^\d{1,8}$",
        message="El RUN debe tener entre 1 y 8 dígitos (sin puntos)."
    )
    run_dv_validator = RegexValidator(
        regex=r"^[0-9Kk]{1}$",
        message="El dígito verificador debe ser 0-9 o K."
    )

    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
        ("N", "Prefiere no decir"),
    ]

    # ---------------------------
    # Identificación
    # ---------------------------
    run_numero = models.CharField(
        "RUN (número)",
        max_length=8,
        validators=[run_numero_validator],
        help_text="Sin puntos ni guión. Ej: 12345678"
    )
    run_dv = models.CharField(
        "DV",
        max_length=1,
        validators=[run_dv_validator],
        help_text="0-9 o K"
    )
    nombres_apellidos = models.CharField("Nombres y Apellidos", max_length=200)
    sexo = models.CharField(
        "Sexo",
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True,
        null=True
    )
    fecha_nacimiento = models.DateField("Fecha Nacimiento", blank=True, null=True)
    edad_anios_meses = models.CharField(
        "Edad (en años y meses)",
        max_length=50,
        blank=True,
        null=True,
        help_text="Ej: 3 años 2 meses / 3a 2m"
    )
    nacionalidad = models.CharField("Nacionalidad", max_length=100, blank=True, null=True)
    lengua_familia_origen = models.CharField(
        "Lengua familia de origen",
        max_length=150,
        blank=True,
        null=True
    )
    lengua_habitual = models.CharField(
        "Lengua que usa habitualmente",
        max_length=150,
        blank=True,
        null=True
    )
    fecha_reevaluacion = models.DateField("Fecha Reevaluación", blank=True, null=True)

    # ---------------------------
    # Estado de Salud General
    # ---------------------------
    peso_kg = models.DecimalField(
        "Peso (kg)",
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )
    talla_cm = models.DecimalField(
        "Talla (cm)",
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(250)]
    )
    imc = models.DecimalField(
        "IMC",
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    # ---------------------------
    # Bloques clínicos
    # ---------------------------
    diagnostico = models.TextField("Diagnóstico", blank=True, null=True)
    indicaciones = models.TextField("Indicaciones", blank=True, null=True)

    # ---------------------------
    # Metadatos
    # ---------------------------
    creado_en = models.DateTimeField("Creado en", auto_now_add=True)
    actualizado_en = models.DateTimeField("Actualizado en", auto_now=True)

    class Meta:
        verbose_name = "Evaluación de Salud"
        verbose_name_plural = "Evaluaciones de Salud"
        indexes = [
            models.Index(fields=["run_numero", "run_dv"]),
            models.Index(fields=["fecha_nacimiento"]),
            models.Index(fields=["fecha_reevaluacion"]),
        ]

    def __str__(self):
        return f"{self.nombres_apellidos} ({self.run_completo})"

    @property
    def run_completo(self):
        return f"{self.run_numero}-{self.run_dv.upper()}"
