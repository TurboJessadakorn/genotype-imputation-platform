# Generated by Django 3.2.4 on 2023-08-09 05:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_ongoingproject_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ongoingproject',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 16, 5, 11, 47, 772132, tzinfo=utc)),
        ),
    ]
