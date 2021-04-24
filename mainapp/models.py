from django.db import models
from locations.models import Room
from person.models import Person


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'Category'

    def __str__(self):
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=30, db_index=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        db_table = 'Firm'

    def __str__(self):
        return self.name


class Model(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория', db_index=True)
    name = models.CharField(max_length=200, verbose_name='Название', db_index=True, unique=True)
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Производитель')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PeriodOfDiagnostics(models.Model):
    period = models.DurationField(verbose_name="период диагностики", blank=False)




class Product(models.Model):
    serialNumber = models.CharField(max_length=30, verbose_name='Серийный номер', unique=True)
    person = models.ForeignKey(Person, models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    number = models.CharField(max_length=150, verbose_name='Заявка в тех.поддержку', blank=True)
    location = models.ForeignKey(Room, models.CASCADE, verbose_name='Кабинет', blank=True, null=True)

    date_of_last_diagnostics = models.DateField(verbose_name="дата последней диагностики",
                                                blank=True, null=True)
    period_of_product_diagnostics = models.ForeignKey(PeriodOfDiagnostics,
                                                      blank=True, null=True, on_delete=models.SET_NULL,
                                                      verbose_name="период диагностики"
                                                      )

    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    @property
    def date_of_planned_diagnostics(self):
        """Возвращает дату следующей диагностики."""
        return self.date_of_last_diagnostics + self.period_of_product_diagnostics.period

    @property
    def days_remain_to_diagnostics(self):
        import datetime
        return self.date_of_planned_diagnostics - datetime.date.today()

    class Meta:
        abstract = True

    def __str__(self):
        return self.serialNumber


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус', db_index=True)
    slug = models.SlugField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Scheduler(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    location = models.ForeignKey(Room, models.CASCADE, verbose_name='Кабинет', blank=True, null=True)
    person = models.ForeignKey(Person, models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        abstract = True
