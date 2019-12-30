from django.forms import ModelForm
from django import forms
from .models import Albuns
from .models import Clientes
from .models import Logins

class FormAlbum(ModelForm):
    class Meta:
        model = Albuns
        fields = '__all__'

        #('Título', 'Duração', 'Ano', 'Número de Músicas', 'Preço')
        #'__all__'
class FormLogin(ModelForm):
	class Meta:
		model = Logins
		fields = '__all__'
		widgets = {
            'password': forms.PasswordInput(),
        }
        
class FormCliente(ModelForm):
	class Meta:
		model = Clientes
		mask = {'cpf': '000.000.000-00'}
		fields = '__all__'


