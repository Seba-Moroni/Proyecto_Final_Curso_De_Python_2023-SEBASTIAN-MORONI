from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #path('home/', views.home, name="Home"),
    #path('tienda/', views.tienda, name="Tienda"),
    path('', views.blog, name="Blog"),
    #path('contacto/', views.contacto, name="Contacto"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
   



    
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)