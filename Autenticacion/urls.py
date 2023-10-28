from django.urls import path, include
from Autenticacion import views
from django.conf import settings
from django.conf.urls.static import static
from .views import VRegistro, cerrar_sesion, logear



urlpatterns = [
    
    #path('home/', views.home, name="Home"),
    #path('tienda/', views.tienda, name="Tienda"),
    #path('blog/', views.blog, name="Blog"),
    # path('', VRegistro.as_view(), name="Autenticacion"),
    # path('', cerrar_sesion(), name="Cerrar_sesion"),
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_Sesion"),
    path('logear', logear, name="Logear"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)