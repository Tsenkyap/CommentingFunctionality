# Generated by Django 2.1 on 2019-02-18 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comment_out', '0002_comment_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 7, 55, 51, 317141, tzinfo=utc)),
        ),
    ]
