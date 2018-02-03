import datetime
from django import forms

from django.forms import ModelForm, TextInput

from registros.models import Empresa
from .models import Transacao, ItemDeLinha

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = '__all__'
