# Generated by Django 3.1.4 on 2021-04-03 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20210403_1026'),
        ('catriges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catrige',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.person', verbose_name='Пользователь'),
        ),
    ]
