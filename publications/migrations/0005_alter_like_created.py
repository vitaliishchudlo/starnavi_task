# Generated by Django 3.2.5 on 2021-07-28 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_alter_like_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 13, 18, 45, 709371, tzinfo=utc)),
        ),
    ]
