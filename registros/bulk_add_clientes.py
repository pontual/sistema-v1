import os
import csv
from random import randint

from django.db import transaction

from registros.models import Empresa

# Run inside python manage.py shell

# from registros.bulk_add_clientes import add_clientes
# add_clientes()

# CLIENTES_CSV = "/home/heitor/sistema/setup/clientes.csv"
CLIENTES_CSV = "C:/Users/heitor/Desktop/emacs-24.3/bin/sistema/setup/clientes.csv"

def randomCNPJ():
    a = randint(2, 29)
    b = randint(2, 900)
    c = randint(2, 900)
    d = randint(2, 99)
    return "{:02d}.{:03d}.{:03d}/0001-{:02d}".format(a, b, c, d)

def randomIE():
    a = randint(102, 599)
    b = randint(2, 900)
    c = randint(2, 900)
    d = randint(0, 9)
    return "{:03d}.{:03d}.{:03d}-{}".format(a, b, c, d)

@transaction.atomic
def add_clientes():
    with open(CLIENTES_CSV, newline='', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Empresa.objects.create(nome=row[0],
                                   rua=row[1],
                                   bairro=row[2],
                                   cidade=row[3],
                                   estado=row[4],
                                   cep=row[5],
                                   contato=row[6],
                                   telefone=row[7],
                                   cadastro_nacional=randomCNPJ(),
                                   cadastro_estadual=randomIE())
