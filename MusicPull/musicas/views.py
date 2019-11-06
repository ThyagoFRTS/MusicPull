from django.shortcuts import render,redirect
from .models import Albuns
from .forms import FormAlbum
# Create your views here.

def listagem(request):
	data = {}
	data['albuns']= Albuns.objects.all()
	return render(request, 'musicas/listagem.html',data)

def cad_album(request):
	form = FormAlbum(request.POST or None)#Verifica se tem coisa
	print('a')
	if form.is_valid():
		form.save()
		return redirect('/albuns')
	return render(request,'musicas/formCa.html',{'form':form})

def ualbum(request, pk):
	data={}
	album = Albuns.objects.get(pk=pk)
	form = FormAlbum(request.POST or None,instance=album)#Verifica se tem coisa
	if form.is_valid():
		form.save()
		return redirect('/Ra')
	data['form']=form
	data['album']=album
	return render(request,'musicas/formCa.html',{'form':form,'album':album})

def dalbum(request, pk):
	album = Albuns.objects.get(pk=pk)
	album.delete()
	return redirect('listagem')
	
