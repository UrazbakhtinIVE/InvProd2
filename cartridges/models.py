from django.db import models
from django.urls import reverse

from mainapp.models import Category, Firm, Product
from person.models import Person
from .managers import CustomCartridgesManager


class CartridgeModel(models.Model):
    BLACK = "black"
    BLUE = "blue"
    YELLOW = "yellow"
    PURPLE = "purple"
    COLORS = (
        (None, "-----"),
        (BLACK, "Черный"),
        (BLUE, "Голубой"),
        (YELLOW, "Желтый"),
        (PURPLE, "Пурпурный"),
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория"
    )
    name = models.CharField(max_length=20, verbose_name="название")
    color = models.CharField(
        choices=COLORS, max_length=12, default=None,
        verbose_name="цвет", null=True)
    firm = models.ForeignKey(
        Firm,
        on_delete=models.CASCADE,
        verbose_name="производитель"
    )
    img = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Модель картриджа"
        verbose_name_plural = "Модели картриджей"

    def __str__(self):
        return self.name


class Cartridge(Product):
    ONREFILL = "onrefill"
    STATUSES = (
        (Product.RESERVED, "В резерве"),
        (Product.WORKING, "В работе"),
        (ONREFILL, "На заправку"),
    )

    model = models.ForeignKey(
        CartridgeModel,
        on_delete=models.CASCADE,
        verbose_name="модель картриджа")
    status = models.CharField(
        choices=STATUSES, max_length=12, default=Product.RESERVED,
        null=True, verbose_name="статус")
    objects = CustomCartridgesManager()

    class Meta:
        verbose_name = "катридж"
        verbose_name_plural = "катриджи"

    def get_absolute_url(self):
        return reverse("cartridge_list")
