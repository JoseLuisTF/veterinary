from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from apps.usuario.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
            }
        ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Apellido',
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email',
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Direcccion',
        }
    ))

    telephone = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Telefono',
        }
    ))

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Documento',
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Contraseña',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repetir Contraseña',
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'password2', 'address', 'telephone')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'telephone',
            'address',
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'telephone': 'Telefono',
            'address': 'Direccion',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
