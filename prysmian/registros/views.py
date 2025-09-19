from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Carga
from .forms import CargaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/login/')
@permission_required('registros.add_carga', raise_exception=True)
def cadastrar_carga(request):
    if request.method == 'POST':
        form = CargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela')
    else:
        form = CargaForm()
    return render(request, 'form.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('registros.view_carga', raise_exception=True)
def listar_cargas(request):
    # Pega o parâmetro de ordenação; padrão: decrescente por data_insercao
    ordenar = request.GET.get('ordenar', '-data_insercao')

    # Query inicial com ordenação
    cargas = Carga.objects.all().order_by(ordenar)

    # Filtros via GET
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    busca = request.GET.get('busca')

    if data_inicio:
        cargas = cargas.filter(data_insercao__gte=data_inicio)
    if data_fim:
        cargas = cargas.filter(data_insercao__lte=data_fim)

    if busca:
        cargas = cargas.filter(
            Q(numero_carga__icontains=busca) |
            Q(modalidade_carga__icontains=busca) |
            Q(numero_equipamento__icontains=busca) |
            Q(setor_insercao__icontains=busca) |
            Q(cliente__icontains=busca) |
            Q(origem__icontains=busca) |
            Q(destino__icontains=busca) |
            Q(transportadora__icontains=busca) |
            Q(placa__icontains=busca) |
            Q(agente__icontains=busca) |
            Q(grupo_operativo__icontains=busca) |
            Q(observacao__icontains=busca)
        )

    formularios = {carga.id: CargaForm(instance=carga) for carga in cargas}

    return render(request, 'tabela.html', {
        'cargas': cargas,
        'formularios': formularios
    })

@login_required(login_url='/login/')
@permission_required('registros.change_carga', raise_exception=True)
def editar_carga(request, carga_id):
    carga = get_object_or_404(Carga, id=carga_id)
    if request.method == 'POST':
        form = CargaForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            messages.success(request, f'Carga #{carga.numero_carga} foi atualizada com sucesso!')
            return redirect('tabela')
        else:
            messages.error(request, 'Erro ao atualizar a carga. Verifique os dados e tente novamente.')
            return redirect('tabela')
    return redirect('tabela')

@login_required(login_url='/login/')
@permission_required('registros.delete_carga', raise_exception=True)
def deletar_carga(request, carga_id):
    if request.method == 'POST':
        carga = get_object_or_404(Carga, id=carga_id)
        carga.delete()
        messages.success(request, f'Carga #{carga.numero_carga} foi excluída com sucesso!')
    return redirect('tabela')


def login_view(request):
    return render(request, 'login.html')

from rest_framework import viewsets
from .models import Carga
from .serializers import CargaSerializer

class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer


import openpyxl
from django.http import HttpResponse
from .models import Carga  # Ou outro modelo que você esteja usando
@login_required(login_url='/login/')
@permission_required('registros.view_carga', raise_exception=True)
def exportar_excel(request):
    # Criação do arquivo Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Cargas"

    # Cabeçalhos da tabela
    headers = [
        'Data', 'Carga Nº', 'Modalidade', 'Equipamento', 'Contrato', 'Setor', 'Cliente', 'Origem', 'Destino',
        'Transportadora', 'Placa', 'Agente', 'Carga no Chão', 'Valor', 'Krona', 'Golden', 'Grupo Op.', 'Obs.', 'Ações'
    ]
    ws.append(headers)

    # Obtendo os dados dos registros
    cargas = Carga.objects.all()  # Ou aplique filtros conforme necessário
    for carga in cargas:
        row = [
            carga.data_insercao.strftime('%d/%m/%Y'),
            carga.numero_carga,
            carga.modalidade_carga,
            carga.numero_equipamento,
            carga.contrato,
            carga.setor_insercao,
            carga.cliente,
            carga.origem,
            carga.destino,
            carga.transportadora,
            carga.placa,
            carga.agente,
            "Sim" if carga.carga_no_chao else "Não",
            carga.valor_carga,
            "Sim" if carga.krona_ok else "Não",
            "Sim" if carga.golden_ok else "Não",
            carga.grupo_operativo,
            carga.observacao,
            ""  # Aqui você pode adicionar dados adicionais, se necessário
        ]
        ws.append(row)

    # Configurar a resposta HTTP para o download
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=cargas.xlsx'
    wb.save(response)
    return response
