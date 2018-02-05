import os
from django.core.files import File
from registros.models import Produto

FOTO_DIR = "C:/users/heitor/sisfotos/"
os.chdir(FOTO_DIR)

def add_produto(codigo, nome, por_caixa):
    Produto.objects.create(codigo=codigo, nome=nome, por_caixa=por_caixa,
                           foto=File(open(codigo + ".jpg", "rb"))).save()

    
