from django.urls import reverse

from mainapp.models import Product, Model
from django.db import models
from mainapp.models import Scheduler, Status
from person.models import Person
from locations.models import Room

CARTRIDGE_STATUSES = (
    ("reserved", "В резерве"),
    ("working", "В работе"),
    ("repair", "На ремонт"),
)


class MonitorModel(Model):
    diagonal = models.IntegerField(verbose_name='Диоганаль')
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Модель монитора'
        verbose_name_plural = 'Модели мониторов'

    def __str__(self):
        return self.name


class Monitor(Product):
    model = models.ForeignKey(MonitorModel, models.CASCADE, verbose_name='Модель монитора', blank=True, null=True)
    status = models.CharField(choices=CARTRIDGE_STATUSES, max_length=12, default="reserved", null=True,
                              verbose_name='Статус')

    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'

    def __str__(self):
        return self.serialNumber

    def get_absolute_url(self):
        return reverse('output_list')


class MonitorScheduler(Scheduler):
    monitor = models.ForeignKey(Monitor, models.CASCADE, verbose_name='Монитор')
    status = models.CharField(choices=CARTRIDGE_STATUSES, max_length=12, default="reserved", null=True,
                              verbose_name='Статус')
    person = models.ForeignKey(Person, models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    location = models.ForeignKey(Room, models.CASCADE, verbose_name='Место расположение', blank=True, null=True)

    class Meta:
        verbose_name = 'Журнал мониторов'
        verbose_name_plural = 'Журналы мониторов'
        db_table = 'MonitorSheduler'

    # def __str__(self):
    #     return self.monitor.serialNumber


class HeadsetModel(Model):
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Модель гарнитуры'
        verbose_name_plural = 'Модели гарнитур'

    def __str__(self):
        return self.name


class Headset(Product):
    model = models.ForeignKey(HeadsetModel, models.CASCADE, verbose_name='Модель гарнитуры')



    class Meta:
        verbose_name = 'Гарнитура'
        verbose_name_plural = 'Гарнитуры'

    def __str__(self):
        return self.serialNumber


class SpeakersModel(Model):
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Модель колонок'
        verbose_name_plural = 'Модели колонок'

    def __str__(self):
        return self.name


class Speakers(Product):
    model = models.ForeignKey(SpeakersModel, models.CASCADE, verbose_name='Динамиков')

    class Meta:
        verbose_name = 'Колонки'
        verbose_name_plural = 'Колонки'

    def __str__(self):
        return self.serialNumber
