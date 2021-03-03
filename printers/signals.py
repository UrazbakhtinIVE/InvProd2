from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Printer, PrinterScheduler


@receiver(post_save, sender=Printer)
def update_scheduler_status_from_printer(sender, instance, **kwargs):
    """Обновляет printerStatus в модели PrinterScheduler
        при обновлении/создании экземпляра в модели Printer"""

    PrinterScheduler.objects.create(
        printer=instance,
        printerStatus=instance.status,
        location=instance.location
    )


@receiver(post_save, sender=PrinterScheduler)
def update_printer_status_from_scheduler(sender, instance, **kwargs):
    """Обновляет status в модели Printer
        при создании экземпляра PrinterScheduler"""

    Printer.objects.filter(pk=instance.printer.pk) \
        .update(status=instance.printerStatus)


