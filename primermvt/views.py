from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse('Hola usuario, bienvenido a la lista de mis familiares')
    
