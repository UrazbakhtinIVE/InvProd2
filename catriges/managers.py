from django.db import models


class CustomCartridgesManager(models.Manager):
    """Менеджер для модели Cartridge, добавляющий дополнительный функционал."""

    def get_black_cartridges(self):
        return self.get_queryset().filter(catrigeModel__color="black")

    def get_blue_cartridges(self):
        return self.get_queryset().filter(catrigeModel__color="blue")

    def get_yellow_cartridges(self):
        return self.get_queryset().filter(catrigeModel__color="yellow")

    def get_purple_cartridges(self):
        return self.get_queryset().filter(catrigeModel__color="purple")