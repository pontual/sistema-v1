import os
import csv

from django.db import transaction

from catalogo.models import MenuPasta

# Run inside python manage.py shell

# from catalogo.import_pastas import import_all_pastas

PASTAS_CSV = "/home/heitor/sistema/catalogo/data_csv/pasta.csv"

@transaction.atomic
def import_all_pastas():
    with open(PASTAS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            MenuPasta.objects.create(nome=row[0])
