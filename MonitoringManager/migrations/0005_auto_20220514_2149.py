# Generated by Django 3.2.13 on 2022-05-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonitoringManager', '0004_alter_events_md5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='md5',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='events',
            name='returnCode',
            field=models.IntegerField(verbose_name='Kod błędu'),
        ),
    ]
