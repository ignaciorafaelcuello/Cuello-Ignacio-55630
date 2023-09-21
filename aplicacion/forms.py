from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DirectorTecnicoForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length = 50, required = True)
    edad = forms.IntegerField(label = 'Edad', required = True)
    numero = forms.CharField(label = 'Puesto', max_length = 25, required = True)
    antiguedad = forms.IntegerField(label = 'Antiguedad', required = True)
    ganado = forms.CharField(label = 'Torneos Ganados', max_length = 150, required = True)
    clubes = forms.CharField(label = 'Equipos Dirigidos', max_length = 300, required = True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label = 'Email del usuario')
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirmar Contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = 'Email del usuario')
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirmar Contraseña', widget = forms.PasswordInput)
    first_name = forms.CharField(label = 'Nombre/s', max_length = 100, required = True)
    last_name = forms.CharField(label = 'Apellido', max_length = 50, required = True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
    

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required = True)