from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Mexico
from .forms import MexicoForm
from rest_framework import viewsets
from .serializers import MexicoSerializer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

@login_required(login_url='/login/')
@permission_required('mexico.view_mexico', raise_exception=True)
def listar_mexico(request):
    # Pegando parâmetro de ordenação (padrão: -fecha_insercion para ordem decrescente)
    ordenar = request.GET.get('ordenar', '-fecha_insercion')

    # Inicializa o queryset com ordenação
    registros = Mexico.objects.all().order_by(ordenar)

    # Filtros via GET
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    busca = request.GET.get('busca')

    # Filtro por data (se fornecido)
    if data_inicio:
        registros = registros.filter(fecha_insercion__gte=data_inicio)
    if data_fim:
        registros = registros.filter(fecha_insercion__lte=data_fim)

    # Filtro de busca genérica
    if busca:
        registros = registros.filter(
            Q(sector__icontains=busca) |
            Q(transportadora__icontains=busca) |
            Q(placa_tracto__icontains=busca) |
            Q(placa_remolque__icontains=busca) |
            Q(cliente__icontains=busca) |
            Q(origen__icontains=busca) |
            Q(destino__icontains=busca) |
            Q(id_localizador__icontains=busca) |
            Q(oficial__icontains=busca)
        )

    # Formulários por registro (para modais de edição)
    formularios = {registro.id: MexicoForm(instance=registro) for registro in registros}

    return render(request, 'mexico/tabela.html', {
        'registros': registros,
        'formularios': formularios,
    })

@login_required(login_url='/login/')
@permission_required('mexico.add_mexico', raise_exception=True)
def cadastrar_mexico(request):
    if request.method == 'POST':
        form = MexicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mexico')
    else:
        form = MexicoForm()
    return render(request, 'mexico/form.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('mexico.change_mexico', raise_exception=True)
def editar_mexico(request, mexico_id):
    registro = get_object_or_404(Mexico, pk=mexico_id)
    if request.method == 'POST':
        form = MexicoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
    return redirect('listar_mexico')

@login_required(login_url='/login/')
@permission_required('mexico.delete_mexico', raise_exception=True)
def deletar_mexico(request, mexico_id):
    if request.method == 'POST':
        registro = get_object_or_404(Mexico, id=mexico_id)
        registro.delete()
        messages.success(request, f'Registro Mexico #{registro.id_localizador} foi excluído com sucesso!')
    return redirect('listar_mexico')

class MexicoViewSet(viewsets.ModelViewSet):
    queryset = Mexico.objects.all()
    serializer_class = MexicoSerializer

import openpyxl
from django.http import HttpResponse
from .models import Mexico

@login_required(login_url='/login/')
@permission_required('mexico.view_mexico', raise_exception=True)
def exportar_excel_mexico(request):
    # Criação do arquivo Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Registros Mexico"

    # Cabeçalhos da tabela
    headers = [
        'Fecha de la inserción', 'Hora', 'Sector', 'Transportadora', 'Placa tracto', 
        'Placa remolque', 'Cliente', 'Origen', 'Destino', 'ID localizador', 
        'Valor carga', 'Carga en el piso', 'Oficial'
    ]
    ws.append(headers)

    # Obtendo os dados dos registros
    registros = Mexico.objects.all()
    for registro in registros:
        row = [
            registro.fecha_insercion.strftime('%d/%m/%Y'),
            registro.hora.strftime('%H:%M'),
            registro.sector,
            registro.transportadora,
            registro.placa_tracto,
            registro.placa_remolque,
            registro.cliente,
            registro.origen,
            registro.destino,
            registro.id_localizador,
            registro.valor_carga,
            registro.carga_en_piso,
            registro.oficial,
        ]
        ws.append(row)

    # Configurar a resposta HTTP para o download
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=registros_mexico.xlsx'
    wb.save(response)
    return response
