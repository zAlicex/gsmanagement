from django.urls import path, include
from . import views
from rest_framework import routers
from .views import SedViewSet

router = routers.DefaultRouter()
router.register(r'sed', SedViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar_sed, name='cadastrar_sed'),
    path('listar/', views.listar_sed, name='listar_sed'),
    path('editar/<int:sed_id>/', views.editar_sed, name='editar_sed'),
    path('api/', include(router.urls)),
]
