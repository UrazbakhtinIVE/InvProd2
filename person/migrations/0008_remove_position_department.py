# Generated by Django 3.1.4 on 2021-04-03 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_remove_person_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='department',
        ),
    ]
