from django import forms
from .models import Usuario, maquina

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'email','usuario','contraseña')

class InicioSesionForm(forms.Form):
    # Campos del formulario de inicio de sesión
    email = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)

class RegistroMaquinaForm(forms.ModelForm):
    class Meta:
        model = maquina
        fields = ('nombre',)
