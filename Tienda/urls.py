from django.urls import path, include
from Tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #path('home/', views.home, name="Home"),
    path('', views.tienda, name="Tienda"),
    #path('blog/', views.blog, name="Blog"),
    #path('contacto/', views.contacto, name="Contacto"),
    
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)