from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Monitor, MonitorScheduler


@receiver(pre_save, sender=Monitor)
def update_scheduler_status_from_monitor(sender, instance, **kwargs):
    """Обновляет monitorStatus в модели monitorScheduler
        при обновлении/создании экземпляра в модели Monitor"""
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.status != instance.status:
            MonitorScheduler.objects.create(
                monitor=instance,
                status=instance.status,
            )

    # print('Hello, World')

