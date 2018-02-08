from django.db import transaction
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from registros.models import Produto

from .models import Item

@transaction.atomic
def import_all():
    produtos = Produto.objects.all()

    for produto in produtos:
        # look for existing Item
        try:
            item = Item.objects.get(produto=produto)
            print("Did not import", produto.codigo, "(already exists)")
        except ObjectDoesNotExist:
            Item.objects.create(produto=produto).save()
            print("Imported", produto.codigo)
            
