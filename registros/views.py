from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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

    try:
        nome = request.POST['nome']
        rua = request.POST['rua']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        cep = request.POST['cep']
        pais = request.POST['pais']
        telefone = request.POST['telefone']
        email = request.POST['email']
        cnpj = request.POST['cnpj']
        inscricao_est = request.POST['inscricao_est']
        inscricao_mun = request.POST['inscricao_mun']
    except KeyError:

        return render(request, 'registros/clientesNovo.html', context)
    else:
        cli_novo = Empresa(nome=nome, rua=rua, cidade=cidade,
                           estado=estado, cep=cep, pais=pais,
                           telefone=telefone, email=email,
                           cadastro_nacional=cnpj,
                           cadastro_estadual=inscricao_est,
                           cadastro_municipal=inscricao_mun)
        cli_novo.save()
        cliente_id = cli_novo.id 
        return HttpResponseRedirect(reverse('registros:clientesVer', kwargs={'cliente_id': cliente_id})) 


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

