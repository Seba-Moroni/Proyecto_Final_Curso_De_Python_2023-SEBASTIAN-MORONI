from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import DatosExtra

@receiver(post_save, sender=User)
def create_datos_extra(sender, instance, created, **kwargs):
    if created:
        DatosExtra.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_datos_extra(sender, instance, **kwargs):
    instance.datosextra.save()
