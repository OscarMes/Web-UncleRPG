from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fnt_inicio(request):

    return render(request, 'unclewebapp/inicio.html')

def fnt_juego1(request):
    return render(request, 'unclewebapp/juego1.html')