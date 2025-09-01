from django.urls import path, include
from . import views
from rest_framework import routers
from .views import SedViewSet
from .views import exportar_excel_sed

router = routers.DefaultRouter()
router.register(r'sed', SedViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar_sed, name='cadastrar_sed'),
    path('listar/', views.listar_sed, name='listar_sed'),
    path('editar/<int:sed_id>/', views.editar_sed, name='editar_sed'),
    path('deletar/<int:sed_id>/', views.deletar_sed, name='deletar_sed'),
    path('api/', include(router.urls)),
    path('exportar-excel/', exportar_excel_sed, name='exportar_excel_sed'),
]
