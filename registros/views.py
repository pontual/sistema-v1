from django.shortcuts import render, get_object_or_404

from .models import Produto, Empresa


def index(request):
    return render(request, 'registros/index.html')


# PRODUTO

def produtos(request):
    context = {'location': 'produtos'}
    return render(request, 'registros/produtos.html', context)


def produtosVer(request):
    context = {'location': 'produtos'}
    return render(request, 'registros/index.html', context)


# CLIENTE

def clientes(request):
    clientes = Empresa.objects.all().order_by('nome')
    
    context = {'location': 'clientes',
               'clientes': clientes}
    return render(request, 'registros/clientes.html', context)


def clientesNovo(request):
    context = {'location': 'clientes'}
    return render(request, 'registros/clientesNovo.html', context)


def clientesVer(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)
    
    context = {'location': 'clientes',
               'cliente': cliente}
    return render(request, 'registros/cliente.html', context)


def clientesEditar(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)

    context = {'location': 'clientes',
               'cliente': cliente}
    return render(request, 'registros/cliente.html', context)


def clientesApagar(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)
    nomeApagado = cliente.nome

    context = {'location': 'clientes',
               'nomeApagado': nomeApagado}
    return render(request, 'registros/clienteApagar.html', context)

