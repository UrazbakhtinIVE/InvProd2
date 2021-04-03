# Generated by Django 3.1.4 on 2021-04-03 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('person', '0005_auto_20210403_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Эл.почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Кабинет'),
            preserve_default=False,
        ),
    ]
