# Generated by Django 3.1.4 on 2021-04-03 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20210403_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('lastName', models.CharField(max_length=100, verbose_name='Имя')),
                ('fatherName', models.CharField(max_length=100, verbose_name='Отчество')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]
