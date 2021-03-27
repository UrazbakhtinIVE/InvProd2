# Generated by Django 3.1.4 on 2021-03-17 13:10

from django.db import migrations, models
import django.db.models.deletion
import printers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catriges', '0001_initial'),
        ('mainapp', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=30, unique=True, verbose_name='Серийный номер')),
                ('name', models.CharField(max_length=20, verbose_name='Имя принтера')),
                ('ip', models.CharField(max_length=15, verbose_name='Ip адрес')),
                ('cartridges', models.ManyToManyField(blank=True, to='catriges.Catrige', verbose_name='Установленый картридж')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Месторасположение')),
            ],
            options={
                'verbose_name': 'Принетер',
                'verbose_name_plural': 'Принтеры',
                'db_table': 'Printer',
            },
        ),
        migrations.CreateModel(
            name='PrinterStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Статус')),
                ('slug', models.SlugField(max_length=20)),
            ],
            options={
                'verbose_name': 'Статус принтера',
                'verbose_name_plural': 'Статусы принтеров',
                'db_table': 'PrinterStatus',
            },
        ),
        migrations.CreateModel(
            name='PrinterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Тип принтера',
                'verbose_name_plural': 'Типы принтеров',
                'db_table': 'PrinterType',
            },
        ),
        migrations.CreateModel(
            name='PrinterScheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('uuid', models.PositiveSmallIntegerField(default=printers.models.random_number, verbose_name='Номер заявки')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printers.printer', verbose_name='Принтер')),
                ('printerStatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='printers.printerstatus', verbose_name='Статус принетра')),
            ],
            options={
                'verbose_name': 'Журнал принтера',
                'verbose_name_plural': 'Журналы принтеров',
                'db_table': 'PrinterSheduler',
            },
        ),
        migrations.CreateModel(
            name='PrinterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Название')),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.firm', verbose_name='Производитель')),
                ('printerType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printers.printertype', verbose_name='Тип принтера')),
            ],
            options={
                'verbose_name': 'Модель принтера',
                'verbose_name_plural': 'Модели принтеров',
                'db_table': 'PrinterModel',
            },
        ),
        migrations.AddField(
            model_name='printer',
            name='printerModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printers.printermodel', verbose_name='Модель принтера'),
        ),
        migrations.AddField(
            model_name='printer',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='printers.printerstatus', verbose_name='Статус принтера'),
        ),
    ]
