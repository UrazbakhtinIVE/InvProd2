from django.db import models

from mainapp.models import Model, Product
from person.models import Person
from locations.models import Room


class MonitorModel(Model):
    photo = models.ImageField(blank=True, null=True)
    diagonal = models.IntegerField(verbose_name="диоганаль")

    class Meta:
        verbose_name = "модель монитора"
        verbose_name_plural = "модели мониторов"


class HeadsetModel(Model):
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "модель гарнитуры"
        verbose_name_plural = "модели гарнитур"


class SpeakersModel(Model):
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "модель колонок"
        verbose_name_plural = "модели колонок"


class Monitor(Product):
    model = models.ForeignKey(
        MonitorModel,
        on_delete=models.CASCADE,
        verbose_name="модель монитора"
    )

    class Meta:
        verbose_name = "монитор"
        verbose_name_plural = "мониторы"


class Headset(Product):
    model = models.ForeignKey(
        HeadsetModel,
        on_delete=models.CASCADE,
        verbose_name="модель гарнитуры"
    )

    class Meta:
        verbose_name = "гарнитура"
        verbose_name_plural = "гарнитуры"


class Speakers(Product):
    model = models.ForeignKey(
        SpeakersModel,
        on_delete=models.CASCADE,
        verbose_name="модель колонок"
    )

    class Meta:
        verbose_name = "колонки"
        verbose_name_plural = "колонки"