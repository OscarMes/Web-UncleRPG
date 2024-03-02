from django.shortcuts import render, get_object_or_404
from .models import Cls_juegos



# Create your views here.

def fnt_inicio(request):
    carta_juego = Cls_juegos.objects.all()

    return render(request, 'unclewebapp/inicio.html', {'juegos' : carta_juego})

def fnt_detalle(request, nombre):
    detalle_juego = get_object_or_404(Cls_juegos, nombre=nombre)
  
    return render(request, 'unclewebapp/detalle.html', {'detalle_juego': detalle_juego})

def fnt_unity(request):

    return render(request,'unclewebapp/unity.html' )