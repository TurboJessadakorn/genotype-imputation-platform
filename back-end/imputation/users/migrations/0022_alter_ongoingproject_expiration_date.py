# Generated by Django 3.2.4 on 2023-08-17 08:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20230816_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ongoingproject',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 8, 31, 51, 170785, tzinfo=utc)),
        ),
    ]
