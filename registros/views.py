from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from movimento.models import ItemDeLinha

from .models import Empresa, Produto, Configuracao
from .forms import ClienteForm, ProdutoForm

def index(request):
    return render(request, 'registros/index.html')


# PAGINATOR SUB-RANGE

def subRange(lastPage, currentPage, width):
    return range(max(1, currentPage-width), min(lastPage, currentPage+width)+1)
    
    
# PRODUTOS

def produtos(request):
    produtos = Produto.objects.all().order_by('codigo')

    PRODUTOS_POR_PAGINA = 8
    LINKS_NO_PAGINATOR = 5
    
    paginator = Paginator(produtos, PRODUTOS_POR_PAGINA)
    page = int(request.GET.get('page', 1))

    try:
        produtos_page = paginator.page(page)
    except PageNotAnInteger:
        produtos_page = paginator.page(1)
    except EmptyPage:
        produtos_page = paginator.page(paginator.num_pages)
        
    context = {'produtos': produtos_page, 'show_page_range': subRange(paginator.num_pages, page, LINKS_NO_PAGINATOR)}
    return render(request, 'registros/produtos/todos.html', context)


def produtosNovo(request):
    context = {}

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto_novo = form.save()
            produto_id = produto_novo.id 
            return HttpResponseRedirect(reverse('registros:produtosVer', kwargs={'produto_id': produto_id}))
        else:
            erro_descricao = form
            return render(request, 'sitewide/erro.html',
                          {'erro_descricao': erro_descricao})
    else:
        form = ProdutoForm()
        context['form'] = form
    
    return render(request, 'registros/produtos/novo.html', context)
    

def produtosVer(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    context = {'produto': produto}
    return render(request, 'registros/produtos/ver.html', context)


def produtosEditar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('registros:produtosVer', kwargs={'produto_id': produto_id}))
        else:
            erro_descricao = form
            return render(request, 'sitewide/erro.html',
                          {'erro_descricao': erro_descricao})
    else:
        form = ProdutoForm(instance=produto)
        return render(request, 'registros/produtos/editar.html', {'form': form})


def produtosConfirmarApagar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    context = {'produto': produto}
    
    return render(request, 'registros/produtos/confirmarApagar.html', context)


def produtosApagar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    
    return HttpResponseRedirect(reverse('registros:produtos'))


# CLIENTES

def clientes(request):
    clientes = Empresa.objects.all().order_by(Lower('nome'))

    CLIENTES_POR_PAGINA = 12
    LINKS_NO_PAGINATOR = 5
    
    paginator = Paginator(clientes, CLIENTES_POR_PAGINA)
    page = int(request.GET.get('page', 1))

    try:
        clientes_page = paginator.page(page)
    except PageNotAnInteger:
        clientes_page = paginator.page(1)
    except EmptyPage:
        clientes_page = paginator.page(paginator.num_pages)
        
    context = {'clientes': clientes_page, 'show_page_range': subRange(paginator.num_pages, page, LINKS_NO_PAGINATOR)}
    return render(request, 'registros/clientes/todos.html', context)


def clientesNovo(request):
    context = {}
    
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente_novo = form.save()
            cliente_id = cliente_novo.id 
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
    vendas = cliente.vendas()
    totais = cliente.totais()
    
    context = {'cliente': cliente, 'vendas': vendas, 'totais': totais}
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
