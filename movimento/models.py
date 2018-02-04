from datetime import date

from django.db import models

from django.db.models import Model
from django.db.models import CharField, IntegerField, DateField
from django.db.models import ForeignKey, CASCADE, SET_NULL
from django.contrib.auth.models import User

from registros.models import Moeda, Produto, Empresa

class Transacao(Model):
    vendedor = ForeignKey(Empresa, related_name="empresa_vendedora", on_delete=SET_NULL, null=True)
    comprador = ForeignKey(Empresa, related_name="empresa_compradora", on_delete=SET_NULL, null=True)
    data = DateField(default=date.today)
    moeda = ForeignKey(Moeda, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Transações"
        ordering = ['-data']

    def total(self):
        out = 0
        for item in self.itens.all():
            out += item.preco_unitario * item.qtde
        return out
        
    def __str__(self):
        fmt = "[{}] {} {} --> {} ({} {})"
        return fmt.format(self.id, self.data,
                          self.vendedor, self.comprador,
                          self.moeda, self.total())

class ItemDeLinha(Model):
    transacao = ForeignKey(Transacao, related_name='itens', on_delete=CASCADE)
    qtde = IntegerField(default=0)
    produto = ForeignKey(Produto, on_delete=SET_NULL, null=True)
    preco_unitario = IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Itens de Linha"

    def total(self):
        return self.qtde * self.preco_unitario
    
    def __str__(self):
        fmt = "[{}] {} pc {} @ {}"
        return fmt.format(self.transacao.id, self.qtde,
                          self.produto, self.preco_unitario)
