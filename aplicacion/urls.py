from django.urls import include, path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = 'home'),
    path('jugadores/', JugadoresList.as_view(), name = 'jugadores'), 
    path('agregarJugador/',agregarJugador.as_view(), name = 'agregarJugador'),
    path('editarJugador/<int:pk>/', editarJugador.as_view(), name = 'editarJugador'),
    path('borrarJugador/<int:pk>/', borrarJugador.as_view(), name = 'borrarJugador'),
    
    path('estadio/', estadio, name = 'estadio'),
    path('sociosForm/', sociosForm, name = 'sociosForm'),

    path('buscarJugador/', buscarJugador, name = 'buscarJugador'),
    path('buscar2/', buscar2, name = 'buscar2'),

    path('director_tecnico/', director_tecnico, name = 'director_tecnico'),
    path('updateDT/<id_dt>/', updateDT, name = 'updateDT'),
    path('deleteDT/<id_dt>/', deleteDT, name = 'deleteDT'),
    path('createDT/', createDT, name = 'createDT'),

    path('tribunas/', TribunasList.as_view(), name = 'tribunas'),
    path('updateTribuna/<int:pk>/', TribunasUpdate.as_view(), name = 'updateTribuna'),
    path('deleteTribuna/<int:pk>/', TribunasDelete.as_view(), name = 'deleteTribuna'),
    path('createTribuna/',TribunasCreate.as_view(), name = 'createTribuna'),

    path('login/', login_request, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'aplicacion/logout.html'), name = 'logout'),

    path('registro/', register, name = 'registro'),
    path('editarPerfil/', editarPerfil, name = 'editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name = 'agregarAvatar'),

    path('quien_soy/', quien_soy, name = 'quien_soy'),

    path('canciones/', CancionesList.as_view(), name = 'canciones'), 
    path('AgregarCancion/',AgregarCancion.as_view(), name = 'AgregarCancion'),
    path('EditarCancion/<int:pk>/', EditarCancion.as_view(), name = 'EditarCancion'),
    path('BorrarCancion/<int:pk>/', BorrarCancion.as_view(), name = 'BorrarCancion'),

    path('intereses/', InteresesList.as_view(), name = 'intereses'), 
    path('AgregarInteres/',AgregarInteres.as_view(), name = 'AgregarInteres'),
    path('EditarInteres/<int:pk>/', EditarInteres.as_view(), name = 'EditarInteres'),
    path('BorrarInteres/<int:pk>/', BorrarInteres.as_view(), name = 'BorrarInteres'),
    
]
