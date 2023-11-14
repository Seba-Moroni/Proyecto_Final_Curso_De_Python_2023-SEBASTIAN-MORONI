from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Post, Categoria
from .forms import PostForm

def blog(request):
    posts = Post.objects.all()
    return render(request, "Blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "Blog/categoria.html", {"categoria": categoria, "posts": posts})

def agregar_post(request):
    if not request.user.is_anonymous:  
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('Blog')
        else:
            form = PostForm()
        return render(request, 'Blog/agregar_post.html', {'form': form})
    else:
        return HttpResponseForbidden("Acceso no autorizado")


def editar_post(request, post_id):
    if request.user.is_superuser:
        post = Post.objects.get(pk=post_id)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('Blog')
        else:
            form = PostForm(instance=post)
        return render(request, 'Blog/editar_post.html', {'form': form, 'post': post})
    else:
        return HttpResponseForbidden("Acceso no autorizado")

def eliminar_post(request, post_id):
    if request.user.is_superuser:
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('Blog')
    else:
        return HttpResponseForbidden("Acceso no autorizado")
