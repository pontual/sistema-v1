from django.shortcuts import render

from .models import MenuPasta, Lista, Item

def index(request):
    pastas = MenuPasta.objects.all().order_by('nome')
    
    return render(request, 'catalogo/index.html', {'pastas': pastas})


def lista(request, lista_id):
    pastas = MenuPasta.objects.all().order_by('nome')
    lista = Lista.objects.get(pk=lista_id)
    itens = lista.item_set.all()
    
    return render(request, 'catalogo/lista.html',
                  {'pastas': pastas, 'lista_nome': lista.nome, 'itens': itens})


def busca(request):
    pastas = MenuPasta.objects.all().order_by('nome')

    query = request.GET['q']

    if query:
        itens = Item.objects.filter(produto__codigo__icontains=query) | Item.objects.filter(produto__nome__icontains=query)
    else:
        itens = Item.objects.none()

    return render(request, 'catalogo/busca_resultado.html',
                  {'query': query, 'itens': itens, 'pastas': pastas})
