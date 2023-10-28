from django.urls import path, include
from   .  import views

app_name="Carrito"

urlpatterns = [
    
    #path('home/', views.home, name="Home"),
    #path('', views.tienda, name="Tienda"),
    #path('blog/', views.blog, name="Blog"),
    #path('contacto/', views.contacto, name="Contacto"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),
    
    
    
]

