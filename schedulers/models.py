from django.db import models

from locations.models import Room
from person.models import Person
from printers.models import Printer, PrinterStatus
from mainapp.models import Product
from cartridges.models import Cartridge
from devices.models import Monitor, Speakers, Headset


class Scheduler(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="дата")
    location = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name="кабинет",
        blank=True, null=True
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    date_of_last_diagnostics = models.DateField(verbose_name="дата последней диагностики",
                                                blank=True, null=True)

    class Meta:
        abstract = True


class PrinterScheduler(Scheduler):
    device = models.ForeignKey(
        Printer,
        on_delete=models.CASCADE,
        verbose_name="принтер"
    )
    status = models.ForeignKey(
        PrinterStatus,
        on_delete=models.CASCADE,
        verbose_name="статус принетра",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "журнал принтера"
        verbose_name_plural = "журналы принтеров"

    def __str__(self):
        return self.device.serialNumber


class CartridgeScheduler(Scheduler):
    device = models.ForeignKey(
        Cartridge,
        on_delete=models.CASCADE,
        verbose_name="картридж"
    )
    status = models.CharField(
        choices=Cartridge.STATUSES, max_length=12,
        default=Cartridge.RESERVED, null=True,
        verbose_name="cтатус"
    )

    class Meta:
        verbose_name = "журнал картриджа"
        verbose_name_plural = "журналы картриджей"

    def __str__(self):
        return self.device.serialNumber


class MonitorScheduler(Scheduler):
    device = models.ForeignKey(
        Monitor,
        on_delete=models.CASCADE,
        verbose_name="монитор"
    )
    status = models.CharField(
        choices=Monitor.STATUSES, max_length=12,
        default=Monitor.RESERVED, null=True,
        verbose_name="cтатус"
    )

    def __str__(self):
        return self.device.serialNumber

    class Meta:
        verbose_name = "журнал монитора"
        verbose_name_plural = "журналы мониторов"


class SpeakersScheduler(Scheduler):
    device = models.ForeignKey(
        Speakers,
        on_delete=models.CASCADE,
        verbose_name="колонки"
    )
    status = models.CharField(
        choices=Speakers.STATUSES, max_length=12,
        default=Speakers.RESERVED, null=True,
        verbose_name="cтатус"
    )

    def __str__(self):
        return self.device.serialNumber

    class Meta:
        verbose_name = "журнал колонки"
        verbose_name_plural = "журналы колонок"


class HeadsetScheduler(Scheduler):
    device = models.ForeignKey(
        Headset,
        on_delete=models.CASCADE,
        verbose_name="гарнитура"
    )
    status = models.CharField(
        choices=Headset.STATUSES, max_length=12,
        default=Headset.RESERVED, null=True,
        verbose_name="cтатус"
    )

    def __str__(self):
        return self.device.serialNumber

    class Meta:
        verbose_name = "журнал гарнитуры"
        verbose_name_plural = "журналы гарнитур"