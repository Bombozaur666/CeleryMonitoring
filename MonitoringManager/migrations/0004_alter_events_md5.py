# Generated by Django 3.2.13 on 2022-05-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonitoringManager', '0003_alter_events_md5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='md5',
            field=models.IntegerField(),
        ),
    ]