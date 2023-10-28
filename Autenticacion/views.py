from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth  import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


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
            
            return redirect('Home')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'Registro/registro.html', {'form': form}) 
        
        
# class VRegistro(View):
#     def get(self, request):
#         form = UserRegistrationForm()  # Utiliza tu formulario personalizado
#         return render(request, 'Registro/registro.html', {'form': form})

#     def post(self, request):
#         form = UserRegistrationForm(request.POST)  # Utiliza tu formulario personalizado
#         if form.is_valid():
#             usuario = form.save()
#             login(request, usuario)
#             return redirect('Home')
#         else:
#             for msg in form.errors:
#                 messages.error(request, form.errors[msg])
#             return render(request, 'Registro/registro.html', {'form': form})        
           
        
def cerrar_sesion(request):
     logout(request)
     return redirect('Logear')
 
 
def logear (request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contrasenia=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else: 
                messages.error(request, "Usuario no Valido")
    else:
        messages.error(request, "Informacion Incorrecta")            
                
    form=AuthenticationForm()
    return render(request, 'Login/login.html', {'form': form})  