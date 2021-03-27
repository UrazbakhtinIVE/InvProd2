from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Printer, PrinterScheduler


def get_cartridges_instances(instance):
    """Формирует словарь из экземпляров установленных в принтер картриджей."""
    return {
        "black_cartridge": instance.black_cartridge,
        "blue_cartridge": instance.blue_cartridge,
        "yellow_cartridge": instance.yellow_cartridge,
        "purple_cartridge": instance.purple_cartridge,
    }


def update_cartridges_statuses(obj, cartridges):
    """Обновляет статусы установленных в принтер картриджей."""

    for cartridge_name, new_cartridge_instance in cartridges.items():
        old_cartridge_instance = getattr(obj, cartridge_name)

        if new_cartridge_instance != old_cartridge_instance:
            if new_cartridge_instance and new_cartridge_instance.status == "reserved":
                new_cartridge_instance.status = "working"
                new_cartridge_instance.save()
                continue

            if old_cartridge_instance and old_cartridge_instance.status == "working":
                old_cartridge_instance.status = "onrefill"
                old_cartridge_instance.save()
                continue


@receiver(pre_save, sender=Printer)
def update_scheduler_status_from_printer(sender, instance, **kwargs):
    """Обновляет status в модели Catrige
        при обновлении экземпляра Printer"""

    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.status != instance.status:
            PrinterScheduler.objects.create(
                printer=instance,
                printerStatus=instance.status,
                location=instance.location
            )

        cartridges = get_cartridges_instances(instance=instance)
        update_cartridges_statuses(obj=obj, cartridges=cartridges)


@receiver(post_save, sender=Printer)
def update_cartridge_scheduler_status_from_printer(sender, instance, created, **kwargs):
    """Обновляет cartridgeStatus в модели CatrigeScheduler
        при обновлении/создании экземпляра в модели Printer"""

    if created:
        """Обновляет status в модели Catrige при создании экземпляра Printer"""
        cartridges = get_cartridges_instances(instance)

        for cartridge_instance in cartridges.values():
            if cartridge_instance and cartridge_instance.status == "reserved":
                cartridge_instance.status = "working"
                cartridge_instance.save()