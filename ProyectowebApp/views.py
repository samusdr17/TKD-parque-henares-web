from django.shortcuts import render, HttpResponse
from carro.carro import Carro

from servicios.models import Servicio

# Create your views here.

def home(request):

    carro=Carro(request)

    return render(request, "ProyectowebApp/home.html")




