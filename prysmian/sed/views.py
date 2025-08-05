from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Sed
from .forms import SedForm
from rest_framework import viewsets
from .serializers import SedSerializer

def listar_sed(request):
    # Pegando parâmetro de ordenação (padrão: -data para ordem decrescente)
    ordenar = request.GET.get('ordenar', '-data')

    # Inicializa o queryset com ordenação
    registros = Sed.objects.all().order_by(ordenar)

    # Filtros via GET
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    busca = request.GET.get('busca')

    # Filtro por data (se fornecido)
    if data_inicio:
        registros = registros.filter(data__gte=data_inicio)
    if data_fim:
        registros = registros.filter(data__lte=data_fim)

    # Filtro de busca genérica
    if busca:
        registros = registros.filter(
            Q(numero_equipamento__icontains=busca) |
            Q(setor_insercao__icontains=busca) |
            Q(modalidade__icontains=busca) |
            Q(cliente__icontains=busca) |
            Q(origem__icontains=busca) |
            Q(destino__icontains=busca) |
            Q(transportadora__icontains=busca) |
            Q(placa__icontains=busca) |
            Q(agente__icontains=busca)
        )

    # Formulários por registro (para modais de edição)
    formularios = {registro.id: SedForm(instance=registro) for registro in registros}

    return render(request, 'sed/tabela.html', {
        'registros': registros,
        'formularios': formularios,
    })


def cadastrar_sed(request):
    if request.method == 'POST':
        form = SedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_sed')
    else:
        form = SedForm()
    return render(request, 'sed/form.html', {'form': form})


def editar_sed(request, sed_id):
    registro = get_object_or_404(Sed, pk=sed_id)
    if request.method == 'POST':
        form = SedForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
    return redirect('listar_sed')

class SedViewSet(viewsets.ModelViewSet):
    queryset = Sed.objects.all()
    serializer_class = SedSerializer

import openpyxl
from django.http import HttpResponse
from .models import Sed  # Supondo que o modelo do app SED seja 'Sed'

def exportar_excel_sed(request):
    # Criação do arquivo Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Registros SED"

    # Cabeçalhos da tabela
    headers = [
        'Data', 'Equipamento', 'Setor', 'Modalidade', 'Cliente', 'Origem', 'Destino', 
        'Transportadora', 'Placa', 'Agente', 'Carga no Chão', 'Valor', 'Ações'
    ]
    ws.append(headers)

    # Obtendo os dados dos registros
    registros = Sed.objects.all()  # Ou aplique filtros conforme necessário
    for registro in registros:
        row = [
            registro.data.strftime('%d/%m/%Y'),
            registro.numero_equipamento,
            registro.setor_insercao,
            registro.modalidade,
            registro.cliente,
            registro.origem,
            registro.destino,
            registro.transportadora,
            registro.placa,
            registro.agente,
            "Sim" if registro.carga_no_chao else "Não",
            registro.valor_carga,
            ""  # Aqui você pode adicionar dados adicionais, se necessário
        ]
        ws.append(row)

    # Configurar a resposta HTTP para o download
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=registros_sed.xlsx'
    wb.save(response)
    return response
