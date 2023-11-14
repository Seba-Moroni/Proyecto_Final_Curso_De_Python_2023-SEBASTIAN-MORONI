from django.shortcuts import render
from Carrito.carrito import Carro
from django.views.generic import TemplateView


# Create your views here.


def home(request):
    
    carro=Carro(request)
    
    return render(request,"ProyectoWebApp/home.html")




class NosotrosView(TemplateView):
    template_name = 'ProyectoWebApp/nosotros.html'




