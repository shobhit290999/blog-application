# Generated by Django 3.0.5 on 2020-08-26 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200808_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 1, 0, 44, 436232)),
        ),
    ]
