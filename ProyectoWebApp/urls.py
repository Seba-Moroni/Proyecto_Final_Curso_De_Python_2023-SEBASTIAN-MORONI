from django.urls import path, include
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import NosotrosView

urlpatterns = [
    
    path('home/', views.home, name="Home"),   
    path('nosotros/', NosotrosView.as_view(), name='Nosotros'),
    
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)