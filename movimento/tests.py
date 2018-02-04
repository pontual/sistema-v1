from django.test import TestCase

from registros.models import Empresa, Produto, Moeda, Configuracao
from .models import Transacao, ItemDeLinha

class ProdutoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pontual = Empresa.objects.create(nome="Pontual")
        cls.cctc = Empresa.objects.create(nome="CCTC")
        cls.cliente = Empresa.objects.create(nome="Cliente")

        cls.produto_1 = Produto.objects.create(codigo="1", nome="Produto 1", por_caixa=100)
        cls.produto_2 = Produto.objects.create(codigo="2", nome="Produto 2", por_caixa=200)
        
        cls.moeda = Moeda.objects.create(nome="Real", codigo="BRL")

        cls.conf = Configuracao.objects.create(empresa_ativa=cls.pontual)

    def testEstoqueCompra(self):
        compra = Transacao.objects.create(vendedor=self.cctc, comprador=self.pontual, moeda=self.moeda)

        itemCompra = ItemDeLinha.objects.create(transacao=compra, qtde=10000, produto=self.produto_1, preco_unitario=1)

        self.assertEquals(self.produto_1.estoque(), 10000)

    def testEstoqueVenda(self):
        compra = Transacao.objects.create(vendedor=self.cctc, comprador=self.pontual, moeda=self.moeda)

        itemCompra = ItemDeLinha.objects.create(transacao=compra, qtde=200, produto=self.produto_1, preco_unitario=1)

        venda = Transacao.objects.create(vendedor=self.pontual, comprador=self.cliente, moeda=self.moeda)

        itemVenda = ItemDeLinha.objects.create(transacao=venda, qtde=50, produto=self.produto_1, preco_unitario=1)

        self.assertEquals(self.produto_1.estoque(), 150)

class TransacaoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pontual = Empresa.objects.create(nome="Pontual")
        cls.cctc = Empresa.objects.create(nome="CCTC")
        cls.cliente = Empresa.objects.create(nome="Cliente")

        cls.produto_1 = Produto.objects.create(codigo="1", nome="Produto 1", por_caixa=100)
        cls.produto_2 = Produto.objects.create(codigo="2", nome="Produto 2", por_caixa=200)
        
        cls.moeda = Moeda.objects.create(nome="Real", codigo="BRL")

        cls.conf = Configuracao.objects.create(empresa_ativa=cls.pontual)

    def testTransacaoTotal(self):
        compra = Transacao.objects.create(vendedor=self.cctc, comprador=self.pontual, moeda=self.moeda)

        itemCompra_1 = ItemDeLinha.objects.create(transacao=compra, qtde=200, produto=self.produto_1, preco_unitario=10)
        itemCompra_2 = ItemDeLinha.objects.create(transacao=compra, qtde=100, produto=self.produto_2, preco_unitario=30)

        self.assertEquals(compra.total(), 5000)
