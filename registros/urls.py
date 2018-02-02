from django.urls import path

from . import views

app_name = 'registros'

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/ver/<str:codigo>', views.produtosVer, name='produtosVer'),
    
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/novo', views.clientesNovo, name='clientesNovo'),
    path('clientes/ver/<int:cliente_id>', views.clientesVer, name='clientesVer'),
    path('clientes/editar/<int:cliente_id>', views.clientesEditar, name='clientesEditar'),
    path('clientes/confirmar_apagar/<int:cliente_id>', views.clientesConfirmarApagar, name='clientesConfirmarApagar'),
    path('clientes/apagar/<int:cliente_id>', views.clientesApagar, name='clientesApagar'),
]
