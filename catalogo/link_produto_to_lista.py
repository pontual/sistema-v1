import os
import csv

from django.db import transaction

from catalogo.models import Item, Lista

# Run inside python manage.py shell

# from catalogo.link_produto_to_lista import link_produtos

LINK_CSV = "/home/heitor/sistema/catalogo/data_csv/item_lista.csv"

@transaction.atomic
def link_produtos():
    with open(LINK_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            lista = Lista.objects.get(nome=row[0])
            item = Item.objects.get(produto__codigo=row[1])
            # print(item, lista)
            item.listas.add(lista)
