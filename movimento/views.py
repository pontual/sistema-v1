from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Transacao, ItemDeLinha
from .forms import TransacaoForm, ItemDeLinhaFormSet

def index(request):
    return render(request, 'movimento/index.html')


def transacoes(request):
    transacoes = Transacao.objects.all().order_by('-data', '-id')
    
    context = {'transacoes': transacoes}
    return render(request, 'movimento/transacoes/todos.html', context)


def transacoesNovo(request, tipo="padrao"):
    context = {}

    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao_nova = form.save()
            formset = ItemDeLinhaFormSet(request.POST, instance=transacao_nova)
        
            if formset.is_valid():
                formset.save()
                transacao_id = transacao_nova.id
                return HttpResponseRedirect(reverse('movimento:transacoesVer', kwargs={'transacao_id': transacao_id}))
            else:
                erro_descricao = formset
                return render(request, 'sitewide/erro.html',
                              {'erro_descricao': erro_descricao})
        else:
            erro_descricao = form
            return render(request, 'sitewide/erro.html',
                          {'erro_descricao': erro_descricao})
    else:
        if tipo == "venda":
            context['form'] = TransacaoForm(initial={'vendedor': 1})
            context['label'] = "Venda"
        elif tipo == "compra":
            context['form'] = TransacaoForm(initial={'comprador': 1})
            context['label'] = "Compra"
        else:
            # padrao
            context['form'] = TransacaoForm()
            context['label'] = "Transação"
                        
        context['formset'] = ItemDeLinhaFormSet()
    return render(request, 'movimento/transacoes/novo.html', context)
    
def transacoesCompra(request):
    return transacoesNovo(request, "compra")


def transacoesVenda(request):
    return transacoesNovo(request, "venda")


def transacoesVer(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    itensDeLinha = transacao.itens.all()
    
    context = {'transacao': transacao, 'itensDeLinha': itensDeLinha}
    return render(request, 'movimento/transacoes/ver.html', context)


def transacoesEditar(request, transacao_id):
    context = {}
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    context['transacao'] = transacao
    
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


def transacoesConfirmarApagar(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)

    context = {'transacao': transacao}
    return render(request, 'movimento/transacoes/confirmarApagar.html', context)


def transacoesApagar(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    transacao.delete()
    
    return HttpResponseRedirect(reverse('movimento:transacoes'))

