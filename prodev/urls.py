from django.urls import path
from . import views

urlpatterns = [
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registro_maquina/', views.registro_maquina, name='registro_maquina'),
    path('listado_maquinas/', views.listado_maquinas, name='listado_maquinas'),
]
