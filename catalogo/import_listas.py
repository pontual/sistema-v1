import os
import csv

from django.db import transaction

from catalogo.models import Lista

# Run inside python manage.py shell

# from catalogo.import_listas import import_all_listas

LISTAS_CSV = "/home/heitor/sistema/catalogo/data_csv/lista.csv"

@transaction.atomic
def import_all_listas():
    with open(LISTAS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Lista.objects.create(nome=row[0])
