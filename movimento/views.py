from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import inlineformset_factory

from .models import Transacao, ItemDeLinha
from .forms import TransacaoForm

def index(request):
    return render(request, 'movimento/index.html')


def transacoes(request):
    transacoes = Transacao.objects.all().order_by('-data')
    
    context = {'transacoes': transacoes}
    return render(request, 'movimento/transacoes/todos.html', context)


def transacoesNovo(request):
    context = {}

    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao_nova = form.save()
            transacao_id = transacao_nova.id
            return HttpResponseRedirect(reverse('movimento:transacoesVer', kwargs={'transacao_id': transacao_id}))
        else:
            erro_descricao = form
            return render(request, 'sitewide/erro.html',
                          {'erro_descricao': erro_descricao})
    else:
        form = TransacaoForm()
        context['form'] = form
    return render(request, 'movimento/transacoes/novo.html', context)
    

def transacoesVer(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    itensDeLinha = transacao.itens.all()
    
    context = {'transacao': transacao, 'itensDeLinha': itensDeLinha}
    return render(request, 'movimento/transacoes/ver.html', context)


def transacoesEditar(request, transacao_id):
    context = {}
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    context['transacao'] = transacao
    
    ItemDeLinhaFormSet = inlineformset_factory(Transacao, ItemDeLinha, exclude=("transacao", ))
    
    if request.method == "POST":
        form = TransacaoForm(request.POST, instance=transacao)
        formset = ItemDeLinhaFormSet(request.POST, instance=transacao)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return HttpResponseRedirect(reverse('movimento:transacoesVer', kwargs={'transacao_id': transacao_id}))
        else:
            erro_descricao = formset
            return render(request, 'sitewide/erro.html',
                          {'erro_descricao': erro_descricao})
    else:
        context['form'] = TransacaoForm(instance=transacao)
        context['formset'] = ItemDeLinhaFormSet(instance=transacao)
    return render(request, 'movimento/transacoes/editar.html', context)


def transacoesConfirmarApagar(request):
    return render(request, 'movimento/index.html')


def transacoesApagar(request):
    return render(request, 'movimento/index.html')


def compras(request):
    context = {'location': 'compras'}
    return render(request, 'movimento/compras.html', context)


def vendas(request):
    context = {'location': 'vendas'}
    return render(request, 'movimento/vendas.html', context) 
