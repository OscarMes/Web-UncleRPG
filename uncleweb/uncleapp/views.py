from django.shortcuts import render,get_object_or_404
from .models import Tbl_juegos, Tbl_tres_populares
# from .models import Cls_juegos




# Create your views here.

def fnt_inicio(request):
    #consulta todos los elementos de la tabla juegos ordenados por el
    #último elemento agregado (-id) y que solo sean diez ([:10])
    carta_juego = Tbl_juegos.objects.all().order_by('-id')[:10]
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

    #consulta los elementos dentro de la tabla juegos cuyo nombre sea (Unity, RPGMaker...)
    #para consultar el nombre de una llave fornea se debe enlazar la llave foranea con el nombre (__)
    carta_juego_unity = Tbl_juegos.objects.filter(fkidJuegos_idMotor__nombre = 'Unity')

    return render(request,'unclewebapp/unity.html', {'juegos_unity' : carta_juego_unity} )