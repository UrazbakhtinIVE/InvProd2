from mainapp.models import *
from mainapp.models import Scheduler, Product, Model
from locations.models import *
from django.urls import reverse
import  random


class PrinterType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True, unique=True)
    slug = models.SlugField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Тип принтера'
        verbose_name_plural = 'Типы принтеров'
        db_table = 'PrinterType'

    def __str__(self):
        return self.name


class PrinterModel(Model):
    printerType = models.ForeignKey(PrinterType, models.CASCADE, verbose_name='Тип принтера')
    img = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модели принтеров'
        db_table = 'PrinterModel'

    def __str__(self):
        return self.name



class PrinterStatus(Status):
    pass

    class Meta:
        verbose_name = 'Статус принтера'
        verbose_name_plural = 'Статусы принтеров'
        db_table = 'PrinterStatus'



class Printer(Product):
    printerModel = models.ForeignKey(PrinterModel, models.CASCADE, verbose_name='Модель принтера')
    name = models.CharField(max_length=20, verbose_name='Имя принтера')
    ip = models.CharField(max_length=15, verbose_name='Ip адрес')
    status = models.ForeignKey(PrinterStatus,models.CASCADE, verbose_name='Статус принтера', blank=True, null=True)
    location = models.ForeignKey(Room, models.CASCADE, verbose_name='Месторасположение', blank=True, null=True)

    class Meta:
        verbose_name = 'Принетер'
        verbose_name_plural = 'Принтеры'
        db_table = 'Printer'

    def __str__(self):
        return self.serialNumber


    def get_absolute_url(self):
        return reverse('printer_list')



def random_number():
    rand = random.randrange(1000,10001,1)
    return rand

class PrinterScheduler(Scheduler):
    uuid = models.PositiveSmallIntegerField(verbose_name='Номер заявки', default=random_number)
    printer = models.ForeignKey(Printer, models.CASCADE, verbose_name='Принтер')
    printerStatus = models.ForeignKey(PrinterStatus, models.CASCADE, verbose_name='Статус принетра')
    location = models.ForeignKey(Room, models.CASCADE, verbose_name='Место расположение', blank=True, null=True)

    class Meta:
        verbose_name = 'Журнал принтера'
        verbose_name_plural = 'Журналы принтеров'
        db_table = 'PrinterSheduler'

    def __str__(self):
        return str(self.uuid)

    def get_absolute_url(self):
        return reverse('printer_scheduler_list')


    def printer_status_save(self):
        Printer.status.name = self.printerStatus.name




