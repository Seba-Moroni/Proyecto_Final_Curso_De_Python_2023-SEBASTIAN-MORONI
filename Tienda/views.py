from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.


def tienda(request):
    termino_busqueda = request.GET.get('termino_busqueda', '')
    productos = Producto.objects.all()

    if termino_busqueda:
        productos = productos.filter(nombre__icontains=termino_busqueda)

    return render(request, "Tienda/tienda.html", {"productos": productos, "termino_busqueda": termino_busqueda})




@user_passes_test(lambda u: u.is_superuser)
def admin_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Tienda/admin_productos.html', {'productos': productos})




def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Tienda')  
    else:
        form = ProductoForm()
    return render(request, 'Tienda/agregar_producto.html', {'form': form})



def editar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Tienda')  
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Tienda/editar_producto.html', {'form': form, 'producto': producto})



def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('Tienda')  
    return render(request, 'Tienda/eliminar_producto.html', {'producto': producto})


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'Tienda/detalle_producto.html', {'producto': producto})



def buscar_productos(request):
    
    termino_busqueda = request.GET.get('termino_busqueda', '')    
    resultados_busqueda = Producto.objects.filter(nombre__icontains=termino_busqueda)    
    if not resultados_busqueda:
        mensaje = "No se encontro el producto que buscas, vuelve a intentarlo."
    else:
        mensaje = None  

    context = {
        'resultados_busqueda': resultados_busqueda,
        'termino_busqueda': termino_busqueda,
        'mensaje': mensaje,
    }

    return render(request, 'tu_template.html', context)



