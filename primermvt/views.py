from django.shortcuts import render
from django.http import HttpResponse
from primermvt.models import Familiar

# Create your views here.

def saludo(request):
    return HttpResponse('Hola usuario, bienvenido a la lista de mis familiares')

def lista_familiares(request):
    familiares= Familiar.objects.all()
    return render(request, "primermvt/lista_familiares.html", {"familiares": familiares})
