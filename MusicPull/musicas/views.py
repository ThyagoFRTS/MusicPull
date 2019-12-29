from django.shortcuts import render,redirect
from .models import Albuns
from .forms import FormAlbum
# Create your views here.

def listagem(request):
	data = {}
	data['albuns']= Albuns.objects.all()
	cores=['primary','secondary','success','danger','warning','info','dark']
	return render(request, 'musicas/listagem.html',data,cores)

def home(request):
	return render(request,'musicas/home.html')

def cad_album(request):
	form = FormAlbum(request.POST or None)#Verifica se tem coisa
	if form.is_valid():
		form.save()
		return redirect('/')
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
	
