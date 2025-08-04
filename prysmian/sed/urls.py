from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_sed, name='cadastrar_sed'),
    path('listar/', views.listar_sed, name='listar_sed'),
    path('editar/<int:sed_id>/', views.editar_sed, name='editar_sed'),
]
