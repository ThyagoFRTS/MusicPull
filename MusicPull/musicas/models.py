from django.db import models

# Create your models here.

class Albuns (models.Model):
	titulo = models.CharField(max_length=40,verbose_name='Título')
	duracao = models.DurationField(verbose_name='Duração')
	ano = models.IntegerField(verbose_name='Ano')
	num_musicas = models.IntegerField(verbose_name='Número de Músicas')
	preco = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='Preço')
	
	class Meta:
		verbose_name_plural='Albuns'
	def __str__(self):
		return self.titulo


class Musicas (models.Model):
	compositor = models.CharField(max_length=70)
	artista = models.CharField(max_length=70)
	titulo = models.CharField(max_length=40)
	genero = models.CharField(max_length=20)
	duracao = models.DurationField()
	ano = models.IntegerField()
	participacao = models.CharField(max_length=70,blank=True,null=True)
	album = models.ForeignKey(Albuns, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural='Musicas'

	def __str__(self):
		return self.titulo



class Clientes (models.Model):
	nome = models.CharField(max_length=70,verbose_name='Nome')
	sobrenome = models.CharField(max_length=70,verbose_name='Sobrenome',default='')
	cpf = models.CharField(max_length=14,verbose_name='Cpf',default='000.000.000-00')
	

	class Meta:
		verbose_name_plural='Clientes'

	def __str__(self):
		return self.nome

class Vendas (models.Model):
	album = models.ForeignKey(Albuns, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	quantidade = models.IntegerField(default=0)
	valor = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='Valor')

	class Meta:
		verbose_name_plural='Vendas'

	def __str__(self):
		return str(self.cliente)


class Logins (models.Model):
	username = models.CharField(max_length=40,verbose_name='Usuário',default='username')
	password = models.CharField(max_length=40,verbose_name='Senha',default='password')
	some = models.CharField(max_length=40,verbose_name='Descrição',null=True)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True)
	class Meta:
		verbose_name_plural="Logins"

	def __str__(self):
		return self.username