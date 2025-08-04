from django.db import models

class Sed(models.Model):
    CARGA_CHOICES = [
        (True, 'Sim'),
        (False, 'Não'),
    ]

    data = models.DateField()
    numero_equipamento = models.CharField(max_length=100)
    setor_insercao = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    transportadora = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    agente = models.CharField(max_length=100)
    carga_no_chao = models.BooleanField(choices=CARGA_CHOICES, default=False)
    valor_carga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"SED {self.numero_equipamento} - {self.cliente}"

