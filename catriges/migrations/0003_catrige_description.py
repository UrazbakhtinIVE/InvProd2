# Generated by Django 3.1.4 on 2021-04-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catriges', '0002_catrige_period_of_product_diagnostics'),
    ]

    operations = [
        migrations.AddField(
            model_name='catrige',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
