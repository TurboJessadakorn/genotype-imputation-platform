# Generated by Django 3.2.4 on 2023-08-10 07:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_ongoingproject_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ongoingproject',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 7, 50, 2, 961168, tzinfo=utc)),
        ),
    ]
