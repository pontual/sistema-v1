from django.urls import path

from . import views

app_name = 'movimento'

urlpatterns = [
    path('', views.index, name='index'),
    path('compras/', views.compras, name='compras'),
    path('compra/<int:compra_id>', views.compra, name='compra'),
    path('vendas/', views.vendas, name='vendas'),
    path('venda/<int:venda_id>', views.venda, name='venda'),    
]
