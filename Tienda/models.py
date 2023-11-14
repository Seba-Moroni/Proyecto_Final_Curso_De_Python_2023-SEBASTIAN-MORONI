from django.db import models

# Create your models here.


class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now=True)
    updated=models.DateField(auto_now=True)
    
    class Meta():
        verbose_name='CategoriaProd'
        verbose_name_plural='CategoriasProd'
    
    def __str__(self):
        return self.nombre     
        
        
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='Tienda', null=True, blank=True)
    moneda = models.CharField(max_length=3, choices=[('USD', 'Dólar estadounidense'), ('EUR', 'Euros'), ('ARS', 'Pesos Argentinos'), ('BRL', 'Reales')])
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
