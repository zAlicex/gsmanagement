from django.db import models

# Create your models here.

class CostaRica(models.Model):
    fecha_insercion = models.DateField(verbose_name="Fecha de la inserción")
    hora = models.TimeField(verbose_name="Hora")
    sector = models.CharField(max_length=100, verbose_name="Sector")
    transportadora = models.CharField(max_length=100, verbose_name="Transportadora")
    placa_tracto = models.CharField(max_length=20, verbose_name="Placa tracto")
    placa_remolque = models.CharField(max_length=20, verbose_name="Placa remolque")
    cliente = models.CharField(max_length=100, verbose_name="Cliente")
    origen = models.CharField(max_length=100, verbose_name="Origen")
    destino = models.CharField(max_length=100, verbose_name="Destino")
    id_localizador = models.CharField(max_length=100, verbose_name="ID localizador")
    valor_carga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor carga")
    carga_en_piso = models.CharField(max_length=100, verbose_name="Carga en el piso")
    oficial = models.CharField(max_length=100, verbose_name="Oficial")

    def __str__(self):
        return f"Costa Rica {self.id_localizador} - {self.cliente}"

    class Meta:
        verbose_name = "Costa Rica"
        verbose_name_plural = "Costa Rica"
