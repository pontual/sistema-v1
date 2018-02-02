from django.urls import path

from . import views

app_name = 'registros'

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/novo/', views.produtosNovo, name='produtosNovo'),
    path('produtos/ver/<int:produto_id>/', views.produtosVer, name='produtosVer'),
    path('produtos/editar/<int:produto_id>/', views.produtosEditar, name='produtosEditar'),
    path('produtos/confirmar_apagar/<int:produto_id>', views.produtosConfirmarApagar, name='produtosConfirmarApagar'),
    path('produtos/apagar/<int:produto_id>', views.produtosApagar, name='produtosApagar'),
    
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/novo/', views.clientesNovo, name='clientesNovo'),
    path('clientes/ver/<int:cliente_id>/', views.clientesVer, name='clientesVer'),
    path('clientes/editar/<int:cliente_id>/', views.clientesEditar, name='clientesEditar'),
    path('clientes/confirmar_apagar/<int:cliente_id>/', views.clientesConfirmarApagar, name='clientesConfirmarApagar'),
    path('clientes/apagar/<int:cliente_id>/', views.clientesApagar, name='clientesApagar'),
]
