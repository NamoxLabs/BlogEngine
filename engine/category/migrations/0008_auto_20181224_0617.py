# Generated by Django 2.1.4 on 2018-12-24 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_auto_20181224_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='changed',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 6, 17, 17, 466557, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 6, 17, 17, 466512, tzinfo=utc)),
        ),
    ]
