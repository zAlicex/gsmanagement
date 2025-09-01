from . import views
from rest_framework import routers
from .views import CargaViewSet
from django.urls import path, include
from .views import exportar_excel

router = routers.DefaultRouter()
router.register(r'cargas', CargaViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar_carga, name='formulario'),
    path('listar/', views.listar_cargas, name='tabela'),
    path('login/', views.login_view, name='login'),
    path('editar/<int:carga_id>/', views.editar_carga, name='editar_carga'),
    path('deletar/<int:carga_id>/', views.deletar_carga, name='deletar_carga'),
    path('api/', include(router.urls)),
    path('exportar-excel/', exportar_excel, name='exportar_excel'),
]
