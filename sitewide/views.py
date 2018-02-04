from django.shortcuts import render

from registros.models import Configuracao, Empresa, Produto

def index(request):
    confs = Configuracao.objects.get()
    return render(request, 'sitewide/bootstrap/index.html',
                  {'location': 'home',
                   'confs': confs})

def indexMDC(request):
    confs = Configuracao.objects.get()
    return render(request, 'sitewide/mdc/index.html',
                  {'location': 'home',
                   'confs': confs})

def search(request):
    query = request.GET['query']

    try:
        query_int = int(query)

        # Clientes com ID igual
        clientes_com_id = Empresa.objects.filter(id=query_int)
    except:
        clientes_com_id = []

    # Clientes com nome parecido
    clientes_com_nome = Empresa.objects.filter(nome__icontains=query)

    # Produtos com Codigo parecido
    produtos_com_codigo = Produto.objects.filter(codigo__icontains=query)

    # Produtos com nome parecido
    produtos_com_nome = Produto.objects.filter(nome__icontains=query)

    return render(request, 'sitewide/search_results.html',
                  {'clientes_com_id': clientes_com_id,
                   'clientes_com_nome': clientes_com_nome,
                   'produtos_com_codigo': produtos_com_codigo,
                   'produtos_com_nome': produtos_com_nome})
                  
