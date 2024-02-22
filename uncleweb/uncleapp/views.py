from django.shortcuts import render, get_object_or_404
from .models import Cls_juegos



# Create your views here.

def fnt_inicio(request):
    juegos = Cls_juegos.objects.all()

    return render(request, 'unclewebapp/inicio.html', {'juegos' : juegos})

def fnt_detalle(request, id):
    juego = get_object_or_404(Cls_juegos, pk=id)
  
    return render(request, 'unclewebapp/detalle.html', {'id': juego})