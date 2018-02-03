from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Produto, Empresa
from .forms import ClienteForm

def index(request):
    return render(request, 'registros/index.html')


# PRODUTO

def produtos(request):
    produtos = Produto.objects.all().order_by('codigo')

    context = {'produtos': produtos}
    return render(request, 'registros/produtos/todos.html', context)


def produtosNovo(request):
    return render(request, 'registros/index.html')


def produtosVer(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    context = {'produto': produto}
    return render(request, 'registros/produtos/ver.html', context)


def produtosEditar(request, produto_id):
    return render(request, 'registros/index.html')


def produtosConfirmarApagar(request):
    return render(request, 'registros/index.html')


def produtosApagar(request):
    return render(request, 'registros/index.html')

# CLIENTES

def clientes(request):
    clientes = Empresa.objects.all().order_by('nome')
    
    context = {'clientes': clientes}
    return render(request, 'registros/clientes/todos.html', context)


def clientesNovo(request):
    context = {}
    
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
            return render(request, 'sitewide/erro.html',
                          {'erro_descricao': erro_descricao})
    else:
        form = ClienteForm()
        context['form'] = form
    return render(request, 'registros/clientes/novo.html', context)


def clientesVer(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)
    
    context = {'cliente': cliente}
    return render(request, 'registros/clientes/ver.html', context)


def clientesEditar(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)

    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('registros:clientesVer', kwargs={'cliente_id': cliente_id}))
    return render(request, 'registros/clientes/editar.html', {'form': form})


def clientesConfirmarApagar(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)

    context = {'cliente': cliente}
    return render(request, 'registros/clientes/confirmarApagar.html', context)

def clientesApagar(request, cliente_id):
    cliente = get_object_or_404(Empresa, pk=cliente_id)
    cliente.delete()

    return HttpResponseRedirect(reverse('registros:clientes'))
