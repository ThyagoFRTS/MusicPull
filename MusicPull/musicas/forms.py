from django.forms import ModelForm
from .models import Albuns
from .models import Clientes

class FormAlbum(ModelForm):
    class Meta:
        model = Albuns
        fields = '__all__'

        #('Título', 'Duração', 'Ano', 'Número de Músicas', 'Preço')
        #'__all__'
        
class FormCliente(ModelForm):
	class Meta:
		model = Clientes
		fields = '__all__'