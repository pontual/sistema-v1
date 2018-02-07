from django.urls import path

from . import views

app_name = 'movimento'

urlpatterns = [
    path('', views.index, name='index'),
    path('transacoes/', views.transacoes, name='transacoes'),
    path('transacoes/novo', views.transacoesNovo, name='transacoesNovo'),
    path('transacoes/ver/<int:transacao_id>/', views.transacoesVer, name='transacoesVer'),
    path('transacoes/editar/<int:transacao_id>/', views.transacoesEditar, name='transacoesEditar'),
    path('transacoes/confirmar_apagar/<int:transacao_id>/', views.transacoesConfirmarApagar, name='transacoesConfirmarApagar'),
    path('transacoes/apagar/<int:transacao_id>/', views.transacoesApagar, name='transacoesApagar'),
    
    path('compras/', views.transacoesCompra, name='transacoesCompra'),

    path('vendas/', views.transacoesVenda, name='transacoesVenda'),
    path('vendaCliente/<int:cliente_id>/', views.transacoesVendaCliente, name='transacoesVendaCliente'),
]
