from django.db import models
from django.urls import reverse

from cartridges.models import Cartridge
from mainapp.models import Product, Model, Category, Status


class PrinterType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", db_index=True, unique=True)
    slug = models.SlugField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Тип принтера"
        verbose_name_plural = "Типы принтеров"

    def __str__(self):
        return self.name


class PrinterModel(Model):
    type = models.ForeignKey(PrinterType, models.CASCADE, verbose_name="Тип принтера")
    img = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Модель принтера"
        verbose_name_plural = "Модели принтеров"

    def __str__(self):
        return self.name


class PrinterStatus(Status):
    class Meta:
        verbose_name = "Статус принтера"
        verbose_name_plural = "Статусы принтеров"


class Printer(Product):
    model = models.ForeignKey(
        PrinterModel,
        on_delete=models.CASCADE,
        verbose_name="модель принтера"
    )
    ip = models.CharField(max_length=15, verbose_name="ip адресc")
    status = models.ForeignKey(
        PrinterStatus,
        on_delete=models.CASCADE,
        verbose_name="cтатус принтера",
        blank=True, null=True
    )
    paginate_by = 2

    # Установленные картриджи
    black_cartridge = models.OneToOneField(
        Cartridge, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="black_cartridge",
        verbose_name="черный картридж")

    blue_cartridge = models.OneToOneField(
        Cartridge, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="blue_cartridge",
        verbose_name="голубой картридж")

    yellow_cartridge = models.OneToOneField(
        Cartridge, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="yellow_cartridge",
        verbose_name="желтый картридж")

    purple_cartridge = models.OneToOneField(
        Cartridge, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="purple_cartridge",
        verbose_name="пурпурный картридж")

    class Meta:
        verbose_name = "принетер"
        verbose_name_plural = "принтеры"

    def get_absolute_url(self):
        return reverse("printer_list")