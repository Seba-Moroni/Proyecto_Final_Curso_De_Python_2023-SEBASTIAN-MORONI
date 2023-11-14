from .models import DatosExtra
from .forms import UserRegistrationForm, EdicionPerfil
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.decorators import user_passes_test






# Create your views here.


class VRegistro (View):
    
    def get(slef, request):
        
        form = UserRegistrationForm()
        
        return render(request, 'Registro/registro.html', {'form': form})
    
    def post(self, request):
        
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            
            login(request, usuario)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('Home')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'Registro/registro.html', {'form': form}) 
      
   
  
           
        
def cerrar_sesion(request):
     logout(request)
     return redirect('Logear')
 
 
class CustomLoginMixin:
    def login_user(self, request):
        login(request, self.user)

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                mixin = CustomLoginMixin()
                mixin.user = usuario
                mixin.login_user(request)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no Valido")
        else:
            messages.error(request, "Informacion Incorrecta")
    form = AuthenticationForm()
    return render(request, 'Login/login.html', {'form': form})



@login_required
def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = EdicionPerfil(instance=request.user, initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar})
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nueva_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nueva_avatar:
                datos_extra.avatar = nueva_avatar
                print('NO SE GUARDARON LOS DATOS')
            datos_extra.save()
            formulario.save()
            
            return redirect('Ver_Usuarios')
        else:
            print('NO SE GUARDARON LOS DATOS')
    
    return render(request, 'Login/editar_perfil.html', {'formulario':formulario})


class CambiarContrasenia(PasswordChangeView): 
    template_name = 'Login/cambiar_contrasenia.html'
    success_url = reverse_lazy('Ver_Usuarios')
    
    

class VerUsuariosListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'Login/ver_usuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        if self.request.user.is_superuser:
            
            return User.objects.all()
        else:
            
            return User.objects.filter(pk=self.request.user.pk)


@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuario(request, user_id):
    try:
        usuario = User.objects.get(pk=user_id)
        if usuario.is_superuser:
            
            messages.error(request, "No puedes eliminar a un superusuario.")
            return redirect('Ver_Usuarios')
        
        usuario.delete()
        messages.success(request, f"Usuario {usuario.username} eliminado correctamente.")
        return redirect('Ver_Usuarios')
    except User.DoesNotExist:
        messages.error(request, "Usuario no encontrado.")
        return redirect('Ver_Usuarios')   