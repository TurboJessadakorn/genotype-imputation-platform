# Generated by Django 3.2.4 on 2023-08-08 01:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230803_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ongoingproject',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 1, 57, 20, 833020, tzinfo=utc)),
        ),
    ]
