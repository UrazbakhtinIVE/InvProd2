from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Cartridge
from schedulers.models import CartridgeScheduler


@receiver(pre_save, sender=Cartridge)
def update_scheduler_status_from_cartridge(sender, instance, **kwargs):
    """Обновляет cartridgeStatus в модели cartridgeScheduler
        при обновлении/создании экземпляра в модели Cartridge"""

    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.status != instance.status or obj.date_of_last_diagnostics != instance.date_of_last_diagnostics:
            CartridgeScheduler.objects.create(
                device=instance,
                status=instance.status,
                person=instance.person,
                date_of_last_diagnostics=instance.date_of_last_diagnostics
            )
