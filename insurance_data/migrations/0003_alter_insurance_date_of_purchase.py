# Generated by Django 3.2.8 on 2021-10-26 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_data', '0002_auto_20211026_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='date_of_purchase',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
