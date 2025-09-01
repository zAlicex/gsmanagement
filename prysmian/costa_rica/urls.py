from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CostaRicaViewSet
from .views import exportar_excel_costa_rica

router = routers.DefaultRouter()
router.register(r'costa_rica', CostaRicaViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar_costa_rica, name='cadastrar_costa_rica'),
    path('listar/', views.listar_costa_rica, name='listar_costa_rica'),
    path('editar/<int:costa_rica_id>/', views.editar_costa_rica, name='editar_costa_rica'),
    path('deletar/<int:costa_rica_id>/', views.deletar_costa_rica, name='deletar_costa_rica'),
    path('api/', include(router.urls)),
    path('exportar-excel/', exportar_excel_costa_rica, name='exportar_excel_costa_rica'),
]
