"""MusicPull URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from musicas.views import ralbum,cad_album, ualbum, dalbum
from musicas.views import home, about
from musicas.views import cad_cliente, rcliente,ucliente, dcliente


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('aboutus/',about,name="aboutus"),
    path('Ca/', cad_album, name="cA"),
    path('Ra/', ralbum, name="rA"),
    path('Ua/<int:pk>',ualbum, name="updA"),
    path('Da/<int:pk>',dalbum,name="delA"),
    path('Cc/',cad_cliente,name="cC"),
    path('Rc/',rcliente,name="rC"),
    path('Uc/<int:pk>',ucliente,name="updC"),
    path('Dc/<int:pk>',dcliente,name="delC"),

    
]
