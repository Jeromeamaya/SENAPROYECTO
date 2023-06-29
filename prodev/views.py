from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, InicioSesionForm, RegistroMaquinaForm
from .models import Usuario, maquina


def home(request):
    return render(request, 'prodev/registro.html')
def registro_usuarios(request):
    if request.method == 'POST':
        # Procesa los datos del formulario de registroUsuarios.html y guárdalos en la base de datos
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena)
        usuario.save()

        return render(request, 'registro_usuario.html', {'success': True})
    return render(request, 'registro_usuario.html')

def inicio_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request.POST)
        if form.is_valid():
            # Lógica para autenticar al usuario
            return redirect('listado_maquinas')
    else:
        form = InicioSesionForm()
    return render(request, 'prodev/inicio_sesion.html', {'form': form})

def registro_nueva_maquina(request):
    if request.method == 'POST':
        form = RegistroMaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_maquinas')
    else:
        form = RegistroMaquinaForm()
    return render(request, 'prodev/registro_maquina.html', {'form': form})

def estado_maquinas(request):
    maquinas = Maquina.objects.all()
    return render(request, 'prodev/listado_maquinas.html', {'maquinas': maquinas})


# Create your views here.
