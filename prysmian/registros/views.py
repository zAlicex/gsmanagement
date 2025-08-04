from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Carga
from .forms import CargaForm

def cadastrar_carga(request):
    if request.method == 'POST':
        form = CargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela')
    else:
        form = CargaForm()
    return render(request, 'form.html', {'form': form})


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


def editar_carga(request, carga_id):
    carga = get_object_or_404(Carga, id=carga_id)
    if request.method == 'POST':
        form = CargaForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
    return redirect('tabela')


def login_view(request):
    return render(request, 'login.html')
