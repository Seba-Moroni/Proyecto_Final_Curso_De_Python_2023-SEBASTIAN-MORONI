from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import VRegistro, cerrar_sesion, logear, editar_perfil, CambiarContrasenia
from django.contrib.auth.views import LogoutView
from .views import VerUsuariosListView, eliminar_usuario



urlpatterns = [
    
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_Sesion"),
    path('logear', logear, name="Logear"),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('perfil/editar/', editar_perfil, name="Editar_Perfil"),    
    path('ver-usuarios/', VerUsuariosListView.as_view(), name='Ver_Usuarios'),
    path('perfil/editar/contraseña/', CambiarContrasenia.as_view(), name='Cambiar_Contraseña'),
    path('eliminar_usuario/<int:user_id>/', eliminar_usuario, name='eliminar_usuario'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)