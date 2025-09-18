from django.db import models

class Carga(models.Model):
    CONTRATO_CHOICES = [
        ('Retornável', 'Retornável'),
        ('Descartável', 'Descartável'),
        ('N/A', 'N/A'),
    ]
    
    data_insercao = models.DateField()
    hora = models.TimeField()
    numero_carga = models.CharField(max_length=100)
    modalidade_carga = models.CharField(max_length=100, blank=True, null=True)
    numero_equipamento = models.CharField(max_length=100)
    setor_insercao = models.CharField(max_length=50)
    cliente = models.CharField(max_length=100, default='PRYSMIAN')
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    transportadora = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    agente = models.CharField(max_length=50)
    contrato = models.CharField(max_length=20, choices=CONTRATO_CHOICES, default='Retornável')
    carga_no_chao = models.CharField(max_length=50)
    valor_carga = models.DecimalField(max_digits=15, decimal_places=2)
    krona_ok = models.BooleanField(default=False)      
    golden_ok = models.BooleanField(default=False)     
    grupo_operativo = models.CharField(max_length=100, blank=True, null=True)  
    observacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.numero_carga} - {self.cliente}"
