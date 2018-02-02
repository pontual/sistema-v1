from django.shortcuts import render

from registros.models import Configuracao

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
