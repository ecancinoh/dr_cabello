from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    ROL_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('DOCTOR', 'Doctor/a'),
        ('RECEPCIONISTA', 'Recepcionista'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
        verbose_name='Usuario'
    )
    rol = models.CharField('Rol', max_length=20, choices=ROL_CHOICES, default='RECEPCIONISTA')
    telefono = models.CharField('Teléfono', max_length=20, blank=True, null=True)
    activo = models.BooleanField('Activo', default=True)
    creado_en = models.DateTimeField('Creado en', auto_now_add=True)
    actualizado_en = models.DateTimeField('Actualizado en', auto_now=True)

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'

    def __str__(self):
        return f'{self.user.get_full_name()} – {self.get_rol_display()}'
