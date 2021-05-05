# Generated by Django 3.1.4 on 2021-05-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodofdiagnostics',
            options={'verbose_name': 'Диагостика устройства', 'verbose_name_plural': 'Диагностика устройств'},
        ),
        migrations.AddField(
            model_name='periodofdiagnostics',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='Название периода'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodofdiagnostics',
            name='period',
            field=models.DurationField(verbose_name='Период диагностики'),
        ),
    ]