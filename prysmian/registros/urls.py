from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_carga, name='formulario'),
    path('listar/', views.listar_cargas, name='tabela'),
    path('login/', views.login_view, name='login'),
    path('editar/<int:carga_id>/', views.editar_carga, name='editar_carga')

]
