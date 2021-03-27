from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Catrige, CatrigeScheduler


@receiver(pre_save, sender=Catrige)
def update_scheduler_status_from_catrige(sender, instance, **kwargs):
    """Обновляет catrigeStatus в модели catrigeScheduler
        при обновлении/создании экземпляра в модели Catrige"""

    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.status != instance.status:
            CatrigeScheduler.objects.create(
                catrige=instance,
                catrigeStatus=instance.status)





