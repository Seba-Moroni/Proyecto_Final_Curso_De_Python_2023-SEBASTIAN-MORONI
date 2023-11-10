"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ProyectoWebApp import views
from Autenticacion import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
     path('', views.logear, name="Logear"),
     
     
    #path('home', views.home, name="Home"),
    
    path('admin/', admin.site.urls),
    
    # Estas URLS Pertenece a la APP ProyectoWebApp
    path('', include('ProyectoWebApp.urls')),
        
    
     # Estas URLS Pertenece a la APP Servicios
    path('servicios/', include('Servicios.urls')),
      
    # Estas URLS Pertenece a la APP Blog
    path('blog/', include('Blog.urls')),
     
     # Estas URLS Pertenece a la APP Contacto
    path('contacto/', include('Contacto.urls')),
    
    # Estas URLS Pertenece a la APP Tienda
    path('tienda/', include('Tienda.urls')),
     
     
     # Estas URLS Pertenece a la APP Carrito
    path('carrito/', include('Carrito.urls')),
    
    
     # Estas URLS Pertenece a la APP Autenticacion
    path('autenticacion/', include('Autenticacion.urls')),    
      
     # Estas URLS Pertenece a la APP Pedidos
    path('pedidos/', include('Pedidos.urls')),    
    
     # Estas URLS Pertenece a la APP ChatMoro
    path('chat/', include('ChatMoro.urls')),   
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
