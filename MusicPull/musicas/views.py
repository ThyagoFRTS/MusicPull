from django.shortcuts import render,redirect
from .models import Albuns
from .models import Clientes
from .models import Logins
from .forms import FormAlbum, FormCliente, FormLogin
# Create your views here.


#---------------------------------SOBRE NÓS-------------------------------
def about(request):
	return render(request, 'musicas/aboutus.html')

def home(request):
	
	return render(request,'musicas/home.html')
#---------------------------------ALBUNS----------------------------------
def ralbum(request):
	data = {}
	data['albuns']= Albuns.objects.all()
	cores=['primary','secondary','success','danger','warning','info','dark']
	return render(request, 'musicas/listagemA.html',data,cores)

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
	return redirect('listagemA')
	
#---------------------------------CLIENTES----------------------------------
def rcliente(request):
	data = {}
	data['clientes']= Clientes.objects.all()
	return render(request, 'musicas/listagemC.html',data)

def cad_cliente(request):
	form = FormCliente(request.POST or None)#Verifica se tem coisa
	form2 = FormLogin(request.POST or None)
	if form.is_valid():
		form.save()
		
		return redirect('/')
	return render(request,'musicas/formCc.html',{'form':form,'form2':form2})

def ucliente(request, pk):
	data={}
	cliente = Clientes.objects.get(pk=pk)
	form = FormCliente(request.POST or None,instance=cliente)#Verifica se tem coisa
	if form.is_valid():
		form.save()
		return redirect('/Rc')
	data['form']=form
	data['cliente']=cliente
	return render(request,'musicas/formCc.html',{'form':form,'cliente':cliente})

def dcliente(request, pk):
	cliente = Clientes.objects.get(pk=pk)
	cliente.delete()
	return redirect('listagemC')

#---------------------------------LOGIN----------------------------------

def cuser(request):
	form = FormLogin(request.POST or None)#Verifica se tem coisa
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'musicas/formCu.html',{'form':form})

def log_in(request):
	
	form = FormLogin(request.POST or None)#Verifica se tem coisa
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'musicas/login.html',{'form':form})