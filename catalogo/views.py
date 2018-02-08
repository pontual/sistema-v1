from django.shortcuts import render

from .models import MenuPasta, Lista

def index(request):
    pastas = MenuPasta.objects.all().order_by('nome')
    
    return render(request, 'catalogo/index.html', {'pastas': pastas})


def lista(request, lista_id):
    pastas = MenuPasta.objects.all().order_by('nome')
    lista = Lista.objects.get(pk=lista_id)
    itens = lista.item_set.all()
    
    return render(request, 'catalogo/lista.html', {'pastas': pastas, 'itens': itens})
