from django.forms import ModelForm, TextInput

from .models import Empresa, Produto

class ClienteForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {'nome': TextInput(attrs={'autofocus': 'autofocus'})}


        
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {'codigo': TextInput(attrs={'autofocus': 'autofocus'})}
        
