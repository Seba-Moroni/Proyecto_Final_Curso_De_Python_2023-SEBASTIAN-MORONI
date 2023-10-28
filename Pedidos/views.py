from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Carrito.carrito import Carro
from Pedidos.models import LineaPedido, Pedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.


@login_required(login_url="/Autenticación/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(            
            producto_id=key, 
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido  
            ))
        
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
        
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,        
                            
                
    )
    
    
    messages.success(request, "El Pedido se ha realizado correctamente")
    return redirect('ProyectoWebApp/home.html')    
    
    
def enviar_mail(**kwargs):
        asunto ="Gascias por el Pedido" 
        mensaje= render_to_string("Pedidos/pedidos.html",{
            "pedido":kwargs.get("pedido"),
            "lineas_pedido":kwargs.get("lineas_pedido"),
            "nombreusuario":kwargs.get("nombreusuario") 
                                            
        })
        
        
        mensaje_texto=strip_tags(mensaje)
        from_email="moroni_sebastian@yahoo.com.ar"
        #to=kwargs.get("emailusuario")
        to="moroni_sebastian@yahoo.com.ar"
        send_mail(asunto, mensaje_texto, from_email,[to],html_message=mensaje)
        