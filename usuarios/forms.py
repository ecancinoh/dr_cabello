from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PerfilUsuario


class UsuarioCrearForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=150)
    last_name = forms.CharField(label='Apellido', max_length=150)
    email = forms.EmailField(label='Email')
    rol = forms.ChoiceField(label='Rol', choices=PerfilUsuario.ROL_CHOICES)
    telefono = forms.CharField(label='Teléfono', max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            PerfilUsuario.objects.create(
                user=user,
                rol=self.cleaned_data['rol'],
                telefono=self.cleaned_data.get('telefono', ''),
            )
        return user


class PerfilUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', max_length=150)
    last_name = forms.CharField(label='Apellido', max_length=150)
    email = forms.EmailField(label='Email')

    class Meta:
        model = PerfilUsuario
        fields = ['rol', 'telefono', 'activo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        perfil = super().save(commit=False)
        perfil.user.first_name = self.cleaned_data['first_name']
        perfil.user.last_name = self.cleaned_data['last_name']
        perfil.user.email = self.cleaned_data['email']
        if commit:
            perfil.user.save()
            perfil.save()
        return perfil
