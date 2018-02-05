from datetime import date

from django.db import models

from django.db.models import Model
from django.db.models import CharField, IntegerField, DateField
from django.db.models import ForeignKey, CASCADE, SET_NULL
from django.contrib.auth.models import User

class Transacao(Model):
    vendedor = ForeignKey('registros.Empresa', related_name="empresa_vendedora", on_delete=SET_NULL, null=True)
    comprador = ForeignKey('registros.Empresa', related_name="empresa_compradora", on_delete=SET_NULL, null=True)
    data = DateField(default=date.today)
    moeda = ForeignKey('registros.Moeda', on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Transações"
        ordering = ['-data']

    def total(self):
        out = 0
        for item in self.itens.all():
            out += item.total()
        return out
        
    def __str__(self):
        fmt = "[{}] {} {} --> {} ({} {})"
        return fmt.format(self.id, self.data,
                          self.vendedor, self.comprador,
                          self.moeda, self.total())

class ItemDeLinha(Model):
    transacao = ForeignKey(Transacao, related_name='itens', on_delete=CASCADE)
    qtde = IntegerField(blank=True, null=True)
    produto = ForeignKey('registros.Produto', on_delete=SET_NULL, null=True)
    preco_unitario = IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Itens de Linha"

    def total(self):
        try:
            return self.qtde * self.preco_unitario
        except TypeError:
            return 0
    
    def __str__(self):
        fmt = "[{}] {} --> {}: {} pc {} @ {} {} = {}"
        return fmt.format(self.transacao.data,
                          self.transacao.vendedor, self.transacao.comprador,
                          self.qtde, self.produto,
                          self.transacao.moeda, self.preco_unitario,
                          self.total())
