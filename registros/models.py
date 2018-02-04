from datetime import date

from django.db import models

from django.db.models import Model
from django.db.models import ImageField, EmailField, DateField
from django.db.models import CharField, IntegerField, BooleanField
from django.db.models import ForeignKey, CASCADE, SET_NULL
from django.contrib.auth.models import User

from movimento.models import ItemDeLinha

class Moeda(Model):
    nome = CharField(max_length=63)
    codigo = CharField(max_length=6, verbose_name="Código")
    mostrar_centavos = BooleanField(default=True)

    def __str__(self):
        return self.codigo

    
class Empresa(Model):
    nome = CharField(max_length=255)

    # Endereço
    rua = CharField(max_length=255, blank=True)
    cidade = CharField(max_length=63, blank=True)
    estado = CharField(max_length=63, blank=True)
    cep = CharField(max_length=15, blank=True, verbose_name="CEP")
    pais = CharField(max_length=31, blank=True, verbose_name="País")

    # Contato
    contato = CharField(max_length=63, blank=True) 
    telefone = CharField(max_length=31, blank=True)
    email = EmailField(blank=True)

    # Cadastros 
    cadastro_nacional = CharField(max_length=35, blank=True, verbose_name="CNPJ")
    cadastro_estadual = CharField(max_length=35, blank=True, verbose_name="Inscrição Estadual")
    cadastro_municipal = CharField(max_length=35, blank=True, verbose_name="Inscrição Municipal")

    # funcionario responsavel pelo cliente
    vendedor = ForeignKey('Funcionario', blank=True, null=True, on_delete=SET_NULL)
    
    class Meta:
        ordering = ['nome'] 

    def compras(self):
        transacoes = self.empresa_compradora.all()
        return transacoes

    def __str__(self):
        return self.nome

class Funcionario(Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    empregador = ForeignKey(Empresa, on_delete=SET_NULL, null=True)

    class Meta:
        ordering = ['user__username'] 
    
    def __str__(self):
        return self.user.username

class Configuracao(Model):
    empresa_ativa = ForeignKey(Empresa, blank=True, null=True, on_delete=SET_NULL)

    class Meta:
        verbose_name_plural = "Configurações"
        
    def __str__(self):
        return self.empresa_ativa.nome


class Produto(Model):
    codigo = CharField(max_length=63, verbose_name="Código")
    nome = CharField(max_length=127)
    por_caixa = IntegerField(default=1)
    foto = ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        ordering = ['codigo'] 

    def estoque(self):
        compras = self.compras()
        vendas = self.vendas()
        estoque = 0

        for compra in compras:
            estoque += compra.qtde

        for venda in vendas:
            estoque -= venda.qtde

        return estoque

    def compras(self):
        empresa_ativa = Configuracao.objects.get().empresa_ativa
        return ItemDeLinha.objects.filter(transacao__comprador=empresa_ativa, produto=self)

    def vendas(self):
        empresa_ativa = Configuracao.objects.get().empresa_ativa
        return ItemDeLinha.objects.filter(transacao__vendedor=empresa_ativa, produto=self)
        
    
    def __str__(self):
        return self.codigo
