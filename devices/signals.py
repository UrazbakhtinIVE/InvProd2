from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Monitor, Headset, Speakers
from schedulers.models import MonitorScheduler, SpeakersScheduler, HeadsetScheduler


@receiver(pre_save, sender=Monitor)
def update_scheduler_status_from_monitor(sender, instance, **kwargs):
    """Обновляет status в модели MonitorScheduler
        при обновлении/создании экземпляра в модели Monitor"""
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.status != instance.status or obj.date_of_last_diagnostics != instance.date_of_last_diagnostics:
            MonitorScheduler.objects.create(
                device=instance,
                status=instance.status,
                location=instance.location,
                person=instance.person,
                date_of_last_diagnostics=instance.date_of_last_diagnostics
            )


@receiver(pre_save, sender=Headset)
def update_scheduler_status_from_headset(sender, instance, **kwargs):
    """Обновляет status в модели HeadsetsScheduler
        при обновлении/создании экземпляра в модели Headset"""
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.status != instance.status or obj.date_of_last_diagnostics != instance.date_of_last_diagnostics:
            HeadsetScheduler.objects.create(
                device=instance,
                status=instance.status,
                location=instance.location,
                person=instance.person,
                date_of_last_diagnostics=instance.date_of_last_diagnostics
            )


@receiver(pre_save, sender=Speakers)
def update_scheduler_status_from_speaker(sender, instance, **kwargs):
    """Обновляет status в модели SpeakersScheduler
        при обновлении/создании экземпляра в модели Speaker"""
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.status != instance.status or obj.date_of_last_diagnostics != instance.date_of_last_diagnostics:
            SpeakersScheduler.objects.create(
                device=instance,
                status=instance.status,
                location=instance.location,
                person=instance.person,
                date_of_last_diagnostics=instance.date_of_last_diagnostics
            )