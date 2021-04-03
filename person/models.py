import locations.models


class Department(locations.models.models.Model):
    name = locations.models.models.CharField(max_length=40, verbose_name='Название отдела')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Position(locations.models.models.Model):
    name = locations.models.models.CharField(max_length=150, verbose_name='Название должности', unique=True)
    leader = locations.models.models.BooleanField(default=False, verbose_name='Руководитель')
    vip = locations.models.models.BooleanField(default=False, verbose_name="Vip-персонал")

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Person(locations.models.models.Model):
    firstName = locations.models.models.CharField(max_length=100, verbose_name='Фамилия')
    lastName = locations.models.models.CharField(max_length=100, verbose_name='Имя')
    fatherName = locations.models.models.CharField(max_length=100, verbose_name='Отчество')
    department = locations.models.models.ForeignKey(Department, locations.models.models.CASCADE, verbose_name='Отдел')
    position = locations.models.models.ForeignKey(Position, locations.models.models.CASCADE, verbose_name='Должность')
    email = locations.models.models.EmailField(verbose_name='Эл.почта')
    workPhone = locations.models.models.CharField(max_length=3, verbose_name='Рабочий телефон')
    mobilePhone = locations.models.models.CharField(max_length=12, verbose_name='Мобильный телефон', blank=True, null=True)
    room = locations.models.models.ForeignKey(locations.models.Room, locations.models.models.CASCADE, verbose_name='Кабинет')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return '%s %s %s'% (self.firstName, self.lastName, self.fatherName)
