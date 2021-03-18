import random
from django.db import models
from django.urls import reverse

from mainapp.models import Category, Firm, Product, Scheduler, Status


class CatrigeStatus(Status):

    class Meta:
        verbose_name = 'Статус картриджа'
        verbose_name_plural = 'Статусы картриджей'

    def __str__(self):
        return self.name


class CartridgeModel(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=20, verbose_name='Название')

    COLORS = (
        (None, "-----"),
        ("black", "Черный"),
        ("red", "Красный"),
        ("blue", "Синий"),
        ("yellow", "Желтый"),
    )

    color = models.CharField(choices=COLORS, max_length=12, default=None, verbose_name='Цвет', null=True)
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Производитель' )
    img = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Модель картриджа'
        verbose_name_plural = 'Модели картриджей'

    def __str__(self):
        return self.name



class Catrige(Product):
    catrigeModel = models.ForeignKey(CartridgeModel, models.CASCADE, verbose_name='Модель картриджа')
    status = models.ForeignKey(CatrigeStatus, models.CASCADE, verbose_name='Статус')


    class Meta:
        verbose_name = 'Катридж'
        verbose_name_plural = 'Катриджи'

    def __str__(self):
        return self.serialNumber

    def get_absolute_url(self):
        return reverse('catrige_list')


def random_number():
    rand = random.randrange(1000,10001,1)
    return rand




class CatrigeScheduler(Scheduler):
    uuid = models.PositiveSmallIntegerField(verbose_name='Номер заявки', default=random_number)
    catrige = models.ForeignKey(Catrige, models.CASCADE, verbose_name='Картридж')
    catrigeStatus = models.ForeignKey(CatrigeStatus, models.CASCADE, verbose_name='Статус принетра', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Журнал картриджей'
        verbose_name_plural = 'Журналы картриджей'


    def __str__(self):
        return  self.catrige.serialNumber