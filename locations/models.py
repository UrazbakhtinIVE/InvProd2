from django.db import models


class Tituls(models.Model):
    number = models.CharField(max_length=4, verbose_name='Номер титула', db_index=True)
    name = models.CharField(max_length=150, verbose_name='Название титула', db_index=True)

    class Meta:
        verbose_name = 'Титул'
        verbose_name_plural = 'Титулы'
        db_table = 'Tituls'

    def __str__(self):
        return self.name



class Room(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер')
    titul = models.ForeignKey(Tituls,models.CASCADE, verbose_name='Титул')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'
        db_table = 'Room'

    def __str__(self):
        return self.number
