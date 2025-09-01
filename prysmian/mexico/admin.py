from django.contrib import admin
from .models import Mexico

@admin.register(Mexico)
class MexicoAdmin(admin.ModelAdmin):
    list_display = ['fecha_insercion', 'hora', 'sector', 'transportadora', 'placa_tracto', 'cliente', 'origen', 'destino']
    list_filter = ['fecha_insercion', 'sector', 'transportadora', 'cliente']
    search_fields = ['id_localizador', 'cliente', 'origen', 'destino']
    date_hierarchy = 'fecha_insercion'
