from django.forms import ModelForm

from .models import Empresa, Produto

class ClienteForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

        
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
