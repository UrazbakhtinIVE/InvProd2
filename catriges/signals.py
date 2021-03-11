from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Catrige, CatrigeScheduler


@receiver(post_save, sender=Catrige)
def update_scheduler_status_from_catrige(sender, instance, **kwargs):
    """Обновляет catrigeStatus в модели catrigeScheduler
        при обновлении/создании экземпляра в модели Catrige"""

    CatrigeScheduler.objects.create(
        catrige=instance,
        catrigeStatus=instance.status
    )


@receiver(post_save, sender=CatrigeScheduler)
def update_printer_status_from_scheduler(sender, instance, **kwargs):
    """Обновляет status в модели Catrige
        при создании экземпляра CatrigeScheduler"""
    Catrige.objects.filter(pk=instance.catrige.pk).update(status=instance.catrige.status)





