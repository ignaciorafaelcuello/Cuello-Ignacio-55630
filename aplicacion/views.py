from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import *
from .forms import DirectorTecnicoForm, RegistroUsuariosForm, UserEditForm, AvatarFormulario
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, 'aplicacion/home.html')

#                       Administracion de los jugadores del plantel (Crear, Editar, Eliminar)

def jugadores(request):
    contexto = {'jugadores': Jugadores.objects.all(), 'titulo': 'Estos son los jugadores'}
    return render(request, 'aplicacion/jugadores.html', contexto)

class JugadoresList(LoginRequiredMixin, ListView):
    model = Jugadores

class agregarJugador(LoginRequiredMixin, CreateView):
    model = Jugadores
    fields = ['nombre', 'edad', 'numero', 'antiguedad', 'ganado', 'clubes']
    success_url = reverse_lazy('jugadores')

class editarJugador(LoginRequiredMixin, UpdateView):
    model = Jugadores
    fields = ['nombre', 'edad', 'numero', 'antiguedad', 'ganado', 'clubes']
    success_url = reverse_lazy('jugadores')

class borrarJugador(LoginRequiredMixin, DeleteView):
    model = Jugadores
    success_url = reverse_lazy('jugadores')

@login_required
def buscarJugador(request):
    return render(request, 'aplicacion/buscarJugador.html')

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        jugadores = Jugadores.objects.filter(nombre__icontains = patron)
        contexto = {'jugadores': jugadores}
        return render(request, 'aplicacion/jugadores.html', contexto)
    return render(request, 'aplicacion/buscarJugador.html')

#                       Administracion del Director Tecnico (Crear, Editar, Eliminar)

@login_required
def director_tecnico(request):
    contexto = {'director_tecnico': Director_tecnico.objects.all()}
    return render(request, 'aplicacion/director_tecnico.html', contexto)

@login_required
def updateDT(request, id_dt):
    dt = Director_tecnico.objects.get(id = id_dt)
    if request.method == 'POST':
        miForm = DirectorTecnicoForm(request.POST)
        if miForm.is_valid():
            dt.nombre = miForm.cleaned_data.get('nombre')
            dt.edad = miForm.cleaned_data.get('edad')
            dt.numero = miForm.cleaned_data.get('numero')
            dt.antiguedad = miForm.cleaned_data.get('antiguedad')
            dt.ganado = miForm.cleaned_data.get('ganado')
            dt.clubes = miForm.cleaned_data.get('clubes')
            dt.save()
            return redirect(reverse_lazy('director_tecnico'))
    else:
        miForm = DirectorTecnicoForm(initial={
            'nombre': dt.nombre,
            'edad': dt.edad,
            'numero': dt.numero,
            'antiguedad': dt.antiguedad,
            'ganado': dt.ganado,
            'clubes': dt.clubes,
        })
    return render(request, 'aplicacion/DirectorTecnicoForm.html', {'form': miForm})

@login_required   
def deleteDT(request, id_dt):
    dt = Director_tecnico.objects.get(id = id_dt)
    dt.delete()
    return redirect(reverse_lazy('director_tecnico'))

@login_required
def createDT(request):
    if request.method == 'POST':
        miForm = DirectorTecnicoForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get('nombre')
            edad = miForm.cleaned_data.get('edad')
            numero = miForm.cleaned_data.get('numero')
            antiguedad = miForm.cleaned_data.get('antiguedad')
            ganado = miForm.cleaned_data.get('ganado')
            clubes = miForm.cleaned_data.get('clubes')
            director_tecnico = Director_tecnico(nombre = nombre,
                                                edad = edad,
                                                numero = numero,
                                                antiguedad = antiguedad,
                                                ganado = ganado,
                                                clubes = clubes)
            director_tecnico.save()
            return redirect(reverse_lazy('director_tecnico'))
    else:
        miForm = DirectorTecnicoForm()   
    return render(request, 'aplicacion/DirectorTecnicoForm.html', {'form': miForm})

#                               Administracion de Tribunas (Crear, Editar, Eliminar)

@login_required
def tribunas(request):
    contexto = {'tribunas': Tribunas.objects.all(), 'titulo': 'Informacion de las capacidades e ingreso'}
    return render(request, 'aplicacion/tribunas.html', contexto)

class TribunasList(LoginRequiredMixin, ListView):
    model = Tribunas

class TribunasCreate(LoginRequiredMixin, CreateView):
    model = Tribunas
    fields = ['nombre', 'capacidad', 'ingreso']
    success_url = reverse_lazy('tribunas')

class TribunasUpdate(LoginRequiredMixin, UpdateView):
    model = Tribunas
    fields = ['nombre', 'capacidad', 'ingreso']
    success_url = reverse_lazy('tribunas')

class TribunasDelete(LoginRequiredMixin, DeleteView):
    model = Tribunas
    success_url = reverse_lazy('tribunas')

def estadio(request):
    contexto = {'estadio': Estadio.objects.all(), 'titulo': 'Historia del estadio Julio Cesar Villagra'}
    return render(request, 'aplicacion/estadio.html', contexto)

'''Formulario para hacerse SOCIO que impacta sobre la base de datos, pero solo se ve con el panel de 
administradores'''
    
@login_required
def sociosForm(request):
    if request.method == 'POST':
        socio = Socios(nombre = request.POST['nombre'],
                       apellido = request.POST['apellido'],
                       dni = request.POST['dni'],
                       email = request.POST['email'],
                       direccion = request.POST['direccion'],
                       numero = request.POST['numero'])
        socio.save()
        return HttpResponse('El registro se realizo de manera correcta')
    return render(request, 'aplicacion/sociosForm.html')

#                                       Login del Usuario

def login_request(request):
    if request.method == 'POST':
        miForm = AuthenticationForm(request, data = request.POST)
        if miForm.is_valid():
             usuario = miForm.cleaned_data.get('username')
             password = miForm.cleaned_data.get('password')
             user = authenticate(username = usuario, password = password)
             if user is not None:
                login(request, user)
                try:
                     avatar = Avatar.objects.get(user = request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.jpg'
                finally:
                    request.session['avatar'] = avatar 
                return render(request, 'aplicacion/base.html', {'mensaje': 'Bienvenido al sitio pirata {usuario}'})
             else:
                 return render(request, 'aplicacion/login.html', {'form': miForm, 'mensaje': f'Los datos ingresados NO SON CORRECTOS'})
        else:
            return render(request, 'aplicacion/login.html', {'form': miForm, 'mensaje': f'Los datos ingresados NO SON CORRECTOS'})
    miForm = AuthenticationForm()
    return render(request, 'aplicacion/login.html', {'form': miForm})

#                   Registro y Edicion de los perfiles de Usuarios

def register(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, 'aplicacion/base.html')        
    else:
        miForm = RegistroUsuariosForm()
    return render(request, 'aplicacion/registro.html', {'form': miForm})    
    
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, 'aplicacion/base.html')
        else:
            return render(request, 'aplicacion/editarPerfil.html', {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance = usuario)
    return render(request, 'aplicacion/editarPerfil.html', {'form': form, 'usuario': usuario.username})

#                   Administracion del avatar (Crear, Editar)

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username = request.user)
            avatarIni = Avatar.objects.filter(user = u)
            if len(avatarIni) > 0:
                for i in range(len(avatarIni)):
                    avatarIni[i].delete()
            avatar = Avatar(user = u, imagen = form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user = request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request, 'aplicacion/base.html')
    else:
        form = AvatarFormulario()
    return render(request, 'aplicacion/agregarAvatar.html', {'form': form})


#                       Presentacion del creador de la pagina


def quien_soy(request):
    contexto = {'quien_soy': Quien_Soy.objects.all(), 'titulo': 'MI HISTORIA'}
    return render(request, 'aplicacion/quien_soy.html', contexto)

def intereses(request):
    contexto = {'canciones': Intereses.objects.all(), 'titulo': 'Estos son mis Intereses y Hobbies'}
    return render(request, 'aplicacion/intereses.html', contexto)

class InteresesList(ListView):
    model = Intereses

class AgregarInteres(LoginRequiredMixin, CreateView):
    model = Intereses
    fields = ['intereses']
    success_url = reverse_lazy('intereses')

class EditarInteres(LoginRequiredMixin, UpdateView):
    model = Intereses
    fields = ['intereses']
    success_url = reverse_lazy('intereses')

class BorrarInteres(LoginRequiredMixin, DeleteView):
    model = Intereses
    success_url = reverse_lazy('intereses')

#                           Sector de las canciones mas populares del Club

def canciones(request):
    contexto = {'canciones': Cancion.objects.all(), 'titulo': 'Estas son las canciones mas populares del club'}
    return render(request, 'aplicacion/canciones.html', contexto)

class CancionesList(LoginRequiredMixin, ListView):
    model = Cancion

class AgregarCancion(LoginRequiredMixin, CreateView):
    model = Cancion
    fields = ['nombre', 'letra']
    success_url = reverse_lazy('canciones')

class EditarCancion(LoginRequiredMixin, UpdateView):
    model = Cancion
    fields = ['nombre', 'letra']
    success_url = reverse_lazy('canciones')

class BorrarCancion(LoginRequiredMixin, DeleteView):
    model = Cancion
    success_url = reverse_lazy('canciones')
