# Generated by Django 3.2.4 on 2023-08-16 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_ongoingproject_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ongoingproject',
            name='resubmit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ongoingproject',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 7, 41, 45, 745917, tzinfo=utc)),
        ),
    ]