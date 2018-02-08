import os
import csv
from random import choice

from django.core.files import File
from django.db import transaction

from registros.models import Produto
from setup.produtos import PRODUTO_LIST

# Run inside python manage.py shell

# from registros.bulk_add_produtos import add_produtos
# add_produtos()

FOTO_DIR = "C:/users/heitor/sisfotos/"
# FOTO_DIR = "/home/heitor/tmp/sisfotos/"

PRODUTOS_NOME_CSV = "C:/users/heitor/Desktop/emacs-24.3/bin/sistema/setup/produtos_nome.csv"
# PRODUTOS_NOME_CSV = "/home/heitor/sistema/setup/produtos_nome.csv"

CAIXA_QTDE = [48, 50, 100, 24, 200]

os.chdir(FOTO_DIR)

def add_produto(codigo, nome, por_caixa):
    Produto.objects.create(codigo=codigo, nome=nome, por_caixa=por_caixa,
                           foto=File(open(codigo + ".jpg", "rb"))).save()


@transaction.atomic
def add_produtos():
    produto_nome = {}
    with open(PRODUTOS_NOME_CSV, newline='', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            print(row[0], row[1])
            produto_nome[row[0]] = row[1]

    for produto in PRODUTO_LIST:
        add_produto(produto, produto_nome[produto], choice(CAIXA_QTDE))
