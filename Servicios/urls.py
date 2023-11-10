from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios, name="Servicios"),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('editar_servicio/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar_servicio/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
]


