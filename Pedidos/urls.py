from django.urls import path
from . import views


urlpatterns = [
    
    path('procesar_pedido/', views.procesar_pedido, name='Procesar_Pedido'),
    
]