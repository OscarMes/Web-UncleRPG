from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fnt_hola(request):

    return render(request, 'unclewebapp/navbar/base.html')

def fnt_ejemplo(request):

    return HttpResponse('Ejemplo')