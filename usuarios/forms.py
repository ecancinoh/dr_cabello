from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario


class UsuarioCrearForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nombre', max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Apellido', max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    rol = forms.ChoiceField(
        label='Rol', choices=PerfilUsuario.ROL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        label='Teléfono', max_length=20, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # La señal ya creó el PerfilUsuario vía get_or_create; solo actualizamos.
            perfil = PerfilUsuario.objects.get(user=user)
            perfil.rol = self.cleaned_data['rol']
            perfil.telefono = self.cleaned_data.get('telefono', '')
            perfil.save()
        return user


class PerfilUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nombre', max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Apellido', max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = PerfilUsuario
        fields = ['rol', 'telefono', 'activo']
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
        }

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
