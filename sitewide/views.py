from django.shortcuts import render

from registros.models import Configuracao

def index(request):
    confs = Configuracao.objects.get()
    return render(request, 'sitewide/index.html',
                  {'location': 'home',
                   'confs': confs})
