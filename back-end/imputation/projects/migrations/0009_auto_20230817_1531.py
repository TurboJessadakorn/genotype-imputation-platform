# Generated by Django 3.2.4 on 2023-08-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20230816_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress',
            field=models.CharField(default='0%', max_length=500),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default='Queueing', max_length=500),
        ),
        migrations.DeleteModel(
            name='NextflowProject',
        ),
    ]
