# Generated by Django 4.2.6 on 2023-10-24 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 13, 11, 58, 233730), verbose_name='время'),
        ),
    ]
