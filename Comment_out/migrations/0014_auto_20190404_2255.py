# Generated by Django 2.2 on 2019-04-04 17:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comment_out', '0013_auto_20190218_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 4, 17, 10, 18, 57434, tzinfo=utc)),
        ),
    ]
