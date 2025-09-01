from django.urls import path, include
from . import views
from rest_framework import routers
from .views import MexicoViewSet
from .views import exportar_excel_mexico

router = routers.DefaultRouter()
router.register(r'mexico', MexicoViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar_mexico, name='cadastrar_mexico'),
    path('listar/', views.listar_mexico, name='listar_mexico'),
    path('editar/<int:mexico_id>/', views.editar_mexico, name='editar_mexico'),
    path('deletar/<int:mexico_id>/', views.deletar_mexico, name='deletar_mexico'),
    path('api/', include(router.urls)),
    path('exportar-excel/', exportar_excel_mexico, name='exportar_excel_mexico'),
]
