from django.shortcuts import render
from Servicios.models import Servicio
from django.shortcuts import render, redirect

from .forms import ServicioForm
# Create your views here.


def servicios(request):
    servicios = Servicio.objects.all()  
    return render(request, "Servicios/servicios.html", {"servicios": servicios})


def agregar_servicio(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ServicioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('Servicios')
        else:
            form = ServicioForm()
        return render(request, 'Servicios/agregar_servicio.html', {'form': form})
    else:
        # Puedes manejar la lógica de acceso no autorizado aquí
        pass


def editar_servicio(request, servicio_id):
    if request.user.is_superuser:
        servicio = Servicio.objects.get(pk=servicio_id)
        if request.method == 'POST':
            form = ServicioForm(request.POST, request.FILES, instance=servicio)
            if form.is_valid():
                form.save()
                return redirect('Servicios')
        else:
            form = ServicioForm(instance=servicio)
        return render(request, 'Servicios/editar_servicio.html', {'form': form, 'servicio': servicio})
    else:
        
        pass


def eliminar_servicio(request, servicio_id):
    if request.user.is_superuser:
        servicio = Servicio.objects.get(pk=servicio_id)
        servicio.delete()
        return redirect('Servicios')
    else:
        
        pass
