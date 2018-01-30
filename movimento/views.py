from django.shortcuts import render


def index(request):
    return render(request, 'movimento/index.html')


def compras(request):
    context = {'location': 'compras'}
    return render(request, 'movimento/compras.html', context)


def compra(request, compra_id):
    context = {'location': 'compras'}
    return render(request, 'movimento/index.html', context)


def vendas(request):
    context = {'location': 'vendas'}
    return render(request, 'movimento/vendas.html', context) 


def venda(request, venda_id):
    context = {'location', 'vendas'}
    return render(request, 'movimento/venda.html', context)
