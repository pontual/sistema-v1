import datetime
from django import forms

from django.forms import ModelForm, TextInput, inlineformset_factory, ChoiceField

from registros.models import Empresa
from .models import Transacao, ItemDeLinha

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = '__all__'

ItemDeLinhaFormSet = inlineformset_factory(Transacao, ItemDeLinha, exclude=("transacao", ))
