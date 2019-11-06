from django.db import models

# Create your models here.

class Albuns (models.Model):
	titulo = models.CharField(max_length=40)
	duracao = models.DurationField()
	ano = models.IntegerField()
	num_musicas = models.IntegerField()
	preco = models.DecimalField(max_digits=7,decimal_places=2)
	

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