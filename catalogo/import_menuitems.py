import os
import csv

from django.db import transaction

from catalogo.models import MenuItem, MenuPasta, Lista

# Run inside python manage.py shell

# from catalogo.import_menuitems import import_all_menuitems

MENUITEMS_CSV = "/home/heitor/sistema/catalogo/data_csv/menu_item.csv"

@transaction.atomic
def import_all_menuitems():
    with open(MENUITEMS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            name = row[2]
            pasta_name = row[0]
            lista_name = row[1]

            pasta = MenuPasta.objects.get(nome=pasta_name)
            lista = Lista.objects.get(nome=lista_name)

            MenuItem.objects.create(nome=name, lista=lista, pasta=pasta)
