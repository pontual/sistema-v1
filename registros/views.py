from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Produto, Empresa
from .forms import ClienteForm

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
    return render(request, 'registros/bootstrap/clientes.html', context)


def clientesNovo(request):
    context = {'location': 'clientes'}

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            rua = form.cleaned_data['rua']
            cidade = form.cleaned_data['cidade']
            estado = form.cleaned_data['estado']
            cep = form.cleaned_data['cep']
            pais = form.cleaned_data['pais']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            cadastro_nacional = form.cleaned_data['cadastro_nacional']
            cadastro_estadual = form.cleaned_data['cadastro_estadual']
            cadastro_municipal = form.cleaned_data['cadastro_municipal']
            vendedor = form.cleaned_data['vendedor']
            
            cli_novo = Empresa(nome=nome, rua=rua, cidade=cidade,
                               estado=estado, cep=cep, pais=pais,
                               telefone=telefone, email=email,
                               cadastro_nacional=cadastro_nacional,
                               cadastro_estadual=cadastro_estadual,
                               cadastro_municipal=cadastro_municipal,
                               vendedor=vendedor)
            cli_novo.save()
            cliente_id = cli_novo.id 
            return HttpResponseRedirect(reverse('registros:clientesVer', kwargs={'cliente_id': cliente_id}))
        else:
            erro_descricao = form
            return render(request, 'sitewide/bootstrap/erro.html',
                          {'erro_descricao': erro_descricao})
    else:
        form = ClienteForm()
        context['form'] = form
    return render(request, 'registros/bootstrap/clientesNovo.html', context)

    """
    # MDC version
    
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
    """

def clientesVer(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)
    
    context = {'location': 'clientes',
               'cliente': cliente}
    return render(request, 'registros/bootstrap/clientesVer.html', context)


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

