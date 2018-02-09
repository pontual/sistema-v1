from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/lista/<int:lista_id>/', views.lista, name='lista'),
    path('busca', views.busca, name='busca'),
]
