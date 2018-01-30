from django.contrib import admin

from . models import Moeda, Produto, Empresa, Funcionario, Configuracao

admin.site.register(Moeda)
admin.site.register(Produto)
admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Configuracao)
