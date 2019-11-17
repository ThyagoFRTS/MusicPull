from django.forms import ModelForm
from .models import Albuns

class FormAlbum(ModelForm):
    class Meta:
        model = Albuns
        fields = '__all__'

        #('Título', 'Duração', 'Ano', 'Número de Músicas', 'Preço')
        #'__all__'
        