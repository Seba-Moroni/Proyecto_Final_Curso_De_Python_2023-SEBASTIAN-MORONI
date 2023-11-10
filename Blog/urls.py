from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('agregar_post/', views.agregar_post, name='agregar_post'),
    path('editar_post/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
]



urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)