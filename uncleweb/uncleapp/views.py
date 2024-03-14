from django.shortcuts import render,get_object_or_404
from .models import Tbl_juegos, Tbl_tres_populares
# from .models import Cls_juegos




# Create your views here.

def fnt_inicio(request):
    carta_juego = Tbl_juegos.objects.all()
    # img_populares = Tbl_tres_populares.objects.all()
    pos_izquierda = Tbl_tres_populares.objects.filter(posicion = 'izquierda').first()
    pos_superior = Tbl_tres_populares.objects.filter(posicion = 'superior').first()
    pos_inferior = Tbl_tres_populares.objects.filter(posicion = 'inferior').first()

    return render(request, 'unclewebapp/inicio.html', {'juegos' : carta_juego,
                                                        'izquierda' : pos_izquierda,
                                                        'superior': pos_superior,
                                                        'inferior': pos_inferior
                                                        })

def fnt_detalle(request, nombre):
    detalle_juego = get_object_or_404(Tbl_juegos, nombre=nombre)
  
    return render(request, 'unclewebapp/detalle.html', {'detalle_juego': detalle_juego})

def fnt_unity(request):

    return render(request,'unclewebapp/unity.html' )