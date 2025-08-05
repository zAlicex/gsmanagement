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
