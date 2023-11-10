from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   biografia = models.CharField(max_length=300)
   avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
   
   class Meta:
        verbose_name='Dato Extra'
        verbose_name_plural='Datos Extras'
        
   def __str__(self):
        return f"Usuario: {self.user.username} | Biografia: {self.biografia}"
