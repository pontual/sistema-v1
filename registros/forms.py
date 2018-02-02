from django.forms import ModelForm

from .models import Empresa

class ClienteForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        
    
