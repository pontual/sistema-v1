from django.shortcuts import render

from .models import MenuPasta

def index(request):
    pastas = MenuPasta.objects.all().order_by('nome')
    
    return render(request, 'catalogo/index.html', {'pastas': pastas})


def lista(request, lista_id):
    pastas = MenuPasta.objects.all().order_by('nome')

    return render(request, 'catalogo/lista.html', {'pastas': pastas})
