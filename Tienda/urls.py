from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name="Tienda"),
    
    # Agrega estas rutas para el panel de administración de productos
    path('admin/productos/', views.admin_productos, name='admin_productos'),
    # Define las rutas para agregar, editar y eliminar productos
    path('admin/productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('admin/productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('detalle_producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('admin/productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
